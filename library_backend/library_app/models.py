from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="Unknown Author", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    covers = models.TextField(blank=True, null=True)
    subject_places = models.CharField(max_length=200, blank=True, null=True)
    subject_times = models.CharField(max_length=200, blank=True, null=True)
    subjects = models.CharField(max_length=200, blank=True, null=True)
    first_publish_year = models.IntegerField(blank=True, null=True)
    edition_count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"
