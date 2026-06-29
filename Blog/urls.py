from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("auth/login/", views.LoginView.as_view(), name='login'),
    path("auth/logout/", views.LogoutView.as_view(), name='logout'),
    path("auth/signup/", views.RegisterView.as_view(), name='signup'),
    path("posts/", views.PostListCreateView.as_view(), name='blog_create_list'),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name='blog_details'),
    path("posts/<int:pk>/likes/", views.LikeCreateView.as_view(), name='update'),
    path("posts/comments/", views.CommentListCreateView.as_view()),
    path("posts/comments/<int:pk>/", views.CommentDetailView.as_view())
#     path("blogposts/<str:title>", views.BlogPostList.as_view, name='list_by_title')
]