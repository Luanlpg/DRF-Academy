from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookGenericSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
