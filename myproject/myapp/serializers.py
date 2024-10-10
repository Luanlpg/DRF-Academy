from rest_framework import serializers
from .models import Book, Author, Review
from datetime import date


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_review_author(self, value):
        if value == Author():
            raise serializers.ValidationError(
                "O autor não pode criticar o próprio livro"
                )
        return value


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    review = ReviewSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "A data de publicação não pode ser no futuro."
                )
        return value
