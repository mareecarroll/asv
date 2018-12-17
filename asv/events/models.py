from django.conf import settings
from django.db import models
from django.utils import timezone

class Director(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return "Director:: Name: %s Email: %s Phone: %s" % (
            self.name, self.email, self.phone
        )

class Section(models.Model):
    name = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Section:: Name: %s Director: %s" % (
            self.name, self.director)

class Location(models.Model):
    """Location model."""
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

class Event(models.Model):
    """Event model."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, blank=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True)
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
