from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title