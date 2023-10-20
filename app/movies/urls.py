from django.urls import path

from .views import MovieDetail, MovieDetailByTitle, MovieList

urlpatterns = [
    path("api/v1/movies/", MovieList.as_view()),
    path("api/v1/movies/<str:pk>/", MovieDetail.as_view()),
    path("api/v1/movies/title/<str:title>/", MovieDetailByTitle.as_view()),
]
