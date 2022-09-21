from django.urls import path


from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics
    path('topics/', views.topics, name='topics'),

    # Specific section for a certain topic
    path('topics/<int:topic_id>', views.topic, name='topic'),

    #Adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

]