from rest_framework import serializers
from .models import Book, Author, BookReview
from datetime import date


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookGenericSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = "__all__"


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = "__all__"

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "A avaliação deve estar entre 1 e 5.")
        return value

    def validate_description(self, value):
        if len(value) > 255:
            raise serializers.ValidationError(
                "Superou o limite de caracteres.")
        return value


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    reviews = BookReviewSerializer()

    class Meta:
        model = Book
        fields = "__all__"

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "A data de publicação não pode ser no futuro."
            )
        return value
