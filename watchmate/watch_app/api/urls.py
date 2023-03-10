from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watch_app.api.views import movie_list, movie_details
from .views import (ReviewList, ReviewDetail, ReviewCreate, WatchListAV,
                                 WatchDetailAV, StreamPlatformAV,
                                 StreamPlatformDetailAV, StreamPlatformVS, UserReview,
                                 WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(),name= 'stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # path('review', ReviewList.as_view(),name= 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create /', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),     # This is going to help us to get reviews for the particular movie
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),       # This is going to help us to access indiviudal review

    path('reviews/', UserReview.as_view(), name='user-review-detail'),

]
