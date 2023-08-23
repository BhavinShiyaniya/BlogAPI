from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like

# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

# Post/Blog Serializer
class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.ReadOnlyField()
    total_like = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


# Like Serializer
class LikeSerializer(serializers.HyperlinkedModelSerializer):
    # post = PostSerializer()
    like_id = serializers.ReadOnlyField()
    class Meta:
        model = Like
        fields = '__all__'