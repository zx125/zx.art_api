from rest_framework.serializers import ModelSerializer
import time
from django.conf import settings
from libs.iPay import alipay,alipay_gateway

from . import models
from rest_framework.serializers import ModelSerializer
class ArtModelSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('id','title','desc','comment_num','up_num','zx_time','user_ico','use_name')


class ArtCatModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id','name')


class ArtTabModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id','name')
