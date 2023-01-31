from django.contrib import admin
from django.urls import path, include
from watch_app.api.views import MovieListAV, MovieDetailAV, StreamPlatformAV


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream')

]
