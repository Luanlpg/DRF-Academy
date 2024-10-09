from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookReview(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews')
    data_review = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.book.title} - {self.rating}"
