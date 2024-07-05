from films.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'films/main-page/', MainPageFilmViewSet)
router.register(r'films/(?P<film_id>\d+)/reviews', ReviewViewSet)
router.register(r'films/(?P<film_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet)