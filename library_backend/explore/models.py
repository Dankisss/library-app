from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    covers = models.URLField()  # Пример за поле, което съдържа линк към корицата
    subject_places = models.CharField(max_length=200)  # Примерно поле за места
    subject_times = models.CharField(max_length=200)  # Примерно поле за време
    subjects = models.CharField(max_length=200)  # Примерно поле за теми

    def __str__(self):
        return self.title
