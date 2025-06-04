from rest_framework import serializers
from bookshelf.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    read = serializers.BooleanField()
    year_read = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
