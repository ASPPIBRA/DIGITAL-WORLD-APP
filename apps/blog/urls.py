from django.urls import path
from apps.blog import views


urlpatterns = [
    path("blog.html", views.blog_post),
    path("blog_post_detail/<int:post_id>/", views.blog_detail, name='blog_post_detail'),
]