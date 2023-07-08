from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'date', 'title', 'author', 'content', 'links')

    def get_author(self, obj):
        return "current user"

    def get_links(self, obj):
        links = []
        if obj.link_1:
            links.append({"text": obj.link_1, "url": obj.link_1})
        if obj.link_2:
            links.append({"text": obj.link_2, "url": obj.link_2})
        if obj.link_3:
            links.append({"text": obj.link_3, "url": obj.link_3})
        return links
