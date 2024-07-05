from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import GenericViewSet
from filmapoisk.permissions import IsAuthorUser
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import mixins
from .serializers import *
from .models import *

 
class CRUDMixin(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    pass


class FilmViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    queryset = Film.objects.prefetch_related('actors', 'genre').all()
    serializer_class = FilmSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class ReviewViewSet(CRUDMixin):
    permission_classes = [IsAdminUser | IsAuthorUser | IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_serializer_class(self):
        if self.request.method in {'POST', 'PUT', 'PATCH'}:
            return CreateReviewSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Review.objects.all()

        review_id = self.kwargs.get('film_id')
        if review_id:
            return queryset.filter(film_id=review_id)
        return queryset
        
class MainPageFilmViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    pagination_class = None
    queryset = Film.objects.all()[:6]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = FilmSerializer

class CommentViewSet(CRUDMixin):
    permission_classes = [IsAdminUser | IsAuthorUser | IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method in {'POST', 'PUT', 'PATCH'}:
            return CreateCommentSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Comment.objects.all()

        review_id = self.kwargs.get('review_id')
        if review_id:
            return queryset.filter(review_id=review_id)
        return queryset
