from django.shortcuts import render

from .models import Topic


def index(request):
    """The home page"""
    return render(request, 'learning_logs/index.html')


def topic(request, topic_id):
    """Show a topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, }
    return render(request, 'learning_logs/topic.html', context)
