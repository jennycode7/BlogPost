from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginApiView.as_view(), name='login'),
    path("logout/", views.LogoutApiView.as_view(), name='logout'),
    path("Signup/", views.SignUpApiView.as_view(), name='signup'),
    path("blogposts", views.BlogPostListCreate.as_view(), name='blog_create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path("blogposts/<str:title>", views.BlogPostList.as_view, name='list_by_title')
]
