from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'date', 'title', 'author', 'content', 'links', 'image')

    def get_author(self, obj):
        return "current user"
