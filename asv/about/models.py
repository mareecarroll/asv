from django.db import models

class President(models.Model):
    """President model."""
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    name = models.TextField()
    deceased = models.BooleanField(default=False)

    def mark_deceased(self):
        """Submit an event."""
        self.deceased = True
        self.save()

    def __str__(self):
        """Return string representation of blog post."""
        if self.start_year == self.end_year:
            year = self.start_year
        else:
            year = "%d-%d" % (self.start_year, self.end_year)
        
        if self.deceased:
            deceased = '*'
        else:
            deceased = ''
        return "Year: %s President: %s%s" % (
            year, 
            self.name, 
            deceased
        )

class HonoraryLifeMember(models.Model):
    """Honorary Life Member model."""
    name = models.TextField()
    deceased = models.BooleanField(default=False)

    def change_name(self, name):
        self.name = name

    def mark_deceased(self):
        self.deceased = True
