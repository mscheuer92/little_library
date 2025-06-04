from rest_framework import serializers
from bookshelf.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    read = serializers.BooleanField()
    year_read = serializers.IntegerField()

    # POST
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    # PUT or PATCH
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.read = validated_data.get('read', instance.read)
        instance.year_read = validated_data.get('year_read', instance.year_read)
        instance.save()
        return instance