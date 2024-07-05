from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

class FilmSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    class Meta: 
        model = Film 
        fields = ('id', 'title', 'content', 'actors', 'genre', 'rate')

class CreateCommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'text', 'review', 'author')

    def create(self, validated_data):
        com = Comment.objects.create(
            author=self.context['request'].user,
            **validated_data
        )
        return com 
    
class CreateReviewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model: Review
        fields = ('__all__')

    def create(self, validated_data):
        rev = Review.objects.create(
            author=self.context['request'].user,
            **validated_data
        )
        return rev