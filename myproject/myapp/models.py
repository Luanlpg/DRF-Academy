from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    review_title = models.CharField(max_length=20)
    review = models.TextField()

    def __str__(self):
        return self.review_title
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    review = models.ForeignKey(Review, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title