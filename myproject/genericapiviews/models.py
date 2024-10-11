from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        related_name='books',
        blank=True,
        null=True,
        on_delete=models.CASCADE
        )
    published_date = models.DateField()

    def __str__(self):
        return self.title
