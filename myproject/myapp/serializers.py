from rest_framework import serializers
from .models import Book, Author, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("A nota deve estar entre 1 e 5.")
        return value

    def validate_review(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("A review deve ter no mínimo 10 caracteres.")
        return value