from rest_framework import serializers
from bookshelf.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Title must be at least 2 characters long')
        return value
    
    def validate_author(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Author must be at least 2 characters long')
        return value
                