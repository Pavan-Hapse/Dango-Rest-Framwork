from django.contrib import admin
from django.urls import path, include
# from watch_app.api.views import movie_list, movie_details
from watch_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(),name= 'stream')

]
