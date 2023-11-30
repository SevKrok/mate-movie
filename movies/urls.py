from rest_framework import routers
from django.urls import path, include

from movies.views import MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]


app_name = "movies"
