from django.contrib import admin
from .models import *


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ('actors', 'genre')


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
