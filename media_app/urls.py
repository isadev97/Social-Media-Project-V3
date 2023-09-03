from django.urls import path
from media_app.views import index_view, submit_post, like_post, profile_view

urlpatterns = [
    path('', index_view, name='index'),
    path('submit-post/', submit_post, name='submit_post'),
    path('like-post/', like_post, name='like_post'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
]