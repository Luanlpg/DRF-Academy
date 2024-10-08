from rest_framework import serializers
from .models import Book, Author
from datetime import date


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("A data de publicação não pode ser no futuro.")
        return value