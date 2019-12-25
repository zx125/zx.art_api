from rest_framework.serializers import ModelSerializer
import time
from django.conf import settings
from libs.iPay import alipay, alipay_gateway

from . import models
from rest_framework.serializers import ModelSerializer


class ArtModelSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('id', 'title', 'desc', 'comment_num', 'up_num', 'zx_time', 'user_ico', 'use_name')


class ArtCatModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class ArtTabModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class ArtDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('title', 'desc', 'content', 'up_num', 'use_name', 'zx_time', 'down_num','user')


class ComSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('user','user_name', 'content', 'zx_time', 'article', 'user', 'parent')
        extra_kwargs = {

            'article': {
                'write_only': True
            },
            'parent': {
                'write_only': True
            },
        }


class ArtComSerializer(ModelSerializer):
    haha = ComSerializer(many=True)

    class Meta:
        model = models.Comment
        fields = ('id', 'user_name', 'content', 'zx_time', 'haha','user')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'user_name': {
                'read_only': True
            },

        }
