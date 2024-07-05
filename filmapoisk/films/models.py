from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Film(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    actors = models.ManyToManyField('Actor', max_length=100)
    genre = models.ManyToManyField('Genre', max_length=100)
    rate = models.IntegerField()

    def __str__(self):
        return self.title 
    
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title 

class Review(models.Model):
    text = models.TextField()
    film = models.ForeignKey('Film', on_delete=models.PROTECT, blank=True, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    score = models.FloatField()

    def __str__(self):
        return self.text 

class Comment(models.Model):
    review = models.ForeignKey('Review', on_delete=models.PROTECT, blank=True, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.text 


