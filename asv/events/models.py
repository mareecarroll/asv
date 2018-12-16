from django.conf import settings
from django.db import models
from django.utils import timezone


class Event(models.Model):
    """Event model."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def submit(self):
        """Submit an event."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Return string representation of blog post."""
        return "%s starts %s and ends %s" % (
            self.title, 
            self.start_time, 
            self.end_time)
