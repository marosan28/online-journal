from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
import re
from django import forms
from .models import Topic, Entry, EmailAddress, EntryModelForm, TopicsForm
from .decorators import user_is_superuser
from django.core.mail import EmailMessage
from .forms import NewsletterForm
from users.models import SubscribedUsers
from .models import validate_non_numeric, validate_special_characters, validate_length, non_numeric



def index(request):
    """The home page"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {
                'topics': topics,
            }
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Display only one topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Introduce a new topic."""
    if request.method == 'POST':
        # POST data entered, process.
        form = TopicsForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Topic successfully added!")
            return redirect('learning_logs:topics')
    else:
        # No data submitted return blank form.
        form = TopicsForm()
    # Show a blank or incomplete form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    """Delete a topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        # POST data submitted, delete topic.
        topic.delete()
        messages.success(request, "Topic successfully deleted!")
        return redirect('learning_logs:topics')
    # Show confirmation form.
    context = {'topic': topic}
    return render(request, 'learning_logs/delete_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """New entry"""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        # No data
        form = EntryModelForm()
    else:
        # Data
        form = EntryModelForm(data=request.POST)
        if form.is_valid():
            # Validate the text field
            text = form.cleaned_data['text']
            non_numeric(text)
            validate_length(text)

            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            messages.success(request, "New entry added successfully!")
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request
        form = EntryModelForm(instance=entry)
    else:
        # POST data submitted
        form = EntryModelForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


# Delete Entry

@login_required
def delete_entry(request, entry_id):
    """Delete an entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Entry deleted successfully!")
        return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic}
    return render(request, 'learning_logs/delete_entry.html', context)


# Newsletter


@user_is_superuser
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"OnlineJournal <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='learning_logs/newsletter.html', context={'form': form})


# Disclaimer


def disclaimer(request):
    return render(request, 'learning_logs/disclaimer.html')

# Terms and Conditions 


def tandc(request):
    return render(request, 'learning_logs/tandc.html')