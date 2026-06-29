from rest_framework import serializers
from .models import Post, Comment, Likes, User
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_field

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id',
                'title',
                'slug',
                'content',
                'status',
                'author',
                'likes_count',
                'comments_count',
                'created_at',
                'published_at',
        ]
        read_only_fields = ['author']


    @extend_schema_field(serializers.IntegerField)
    def get_likes_count(self, obj):
            return obj.likes.count()

    @extend_schema_field(serializers.IntegerField)
    def get_comments_count(self, obj):
            return obj.comments.count()


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'content', 'status']

    # def create(self, validated_data):
    #     user = self.context['request'].user

    #     return Post.objects.create(
    #         author=user,
    #         **validated_data
    #     )


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['post', 'created_at']

class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ['id', 'user', 'post']

        read_only_fields = ['user']