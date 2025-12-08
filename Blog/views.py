from django.shortcuts import render
from rest_framework import generics, status
from .models import BlogPost
from .serializers import BlogPostSerializer, SignUpSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate


# Create your views here.
class BlogPostListCreate(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoginApiView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "logged in successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"message" : "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutApiView(APIView):
    def post(self, request):
        logout(request)

        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
    

class SignUpApiView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)