from rest_framework import serializers
from .models import Book, Author, Review
from datetime import date


class AuthorSerializerMyAPP(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookGenericSerializerMyAPP(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializerMyAPP(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
    
    def validate_description(self, value):
        if len(value) > 255:
            raise serializers.ValidationError("Superou o limite de caracteres.")
        return value


class BookSerializerMyAPP(serializers.ModelSerializer):
    author = AuthorSerializerMyAPP()
    # reviews = ReviewSerializerMyAPP()

    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("A data de publicação não pode ser no futuro.")
        return value
    