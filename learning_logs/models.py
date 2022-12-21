from django.db import models


class Topic(models.Model):
    """Topic the user is interested in."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a model"""
        return self.text


class Entry(models.Model):
    """Learning log entries for a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

        
class EmailAddress(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class TopicSearch(models.Model):
    name = models.CharField(max_length=500)