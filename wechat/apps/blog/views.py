from django.shortcuts import render
from rest_framework.generics import ListAPIView,GenericAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import F,Q
from user.models import User
from rest_framework.views import APIView
from . import serializers
from rest_framework import mixins
# from .filters import BlogFilterSet
from . import models
# 分类筛选：django-filter：filter_backends配置DjangoFilterBackend，再在filter_fields中配置分组筛选的字段
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ArtListAPIView(ListAPIView):
    queryset = models.Article.objects.filter().all()
    serializer_class = serializers.ArtModelSerializer

    # 配置过滤器类
    # filter_backends = [OrderingFilter, LimitFilter]  # LimitFilter自定义过滤器
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    # 参与排序的字段: ordering=-price,id
    ordering_fields = ['created_time', 'up_num']
    # 参与搜索的字段: search=python  (name字段中带python就ok)
    search_fields = ['title', 'desc']
    # 参与分类筛选的字段：所有字段都可以，但是用于分组的字段更有意义
    filter_fields = ('category',)
    # filter_class = BlogFilterSet

    # 分页器
    # pagination_class = CoursePageNumberPagination
    def post(self,request,*args,**kwargs):
        print(request)

class ArtCatListAPIView(ListAPIView):
    queryset = models.Category.objects.filter().all()
    serializer_class = serializers.ArtCatModelSerializer

class ArtTabListAPIView(ListAPIView):
    queryset = models.Tag.objects.filter().all()
    serializer_class = serializers.ArtTabModelSerializer


class ArtDetailListAPIView(RetrieveAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArtDetailSerializer

class ArtComListAPIView(ListAPIView):
    #jwt
    authentication_classes = [JSONWebTokenAuthentication]

    queryset = models.Comment.objects.filter(parent=1).all()
    serializer_class = serializers.ArtComSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ('article',)
    def post(self,request,*args,**kwargs):

        data = request.data
        data['user'] = request.user.id
        print(data)
        com_ser = serializers.ComSerializer(data=data)
        if com_ser.is_valid():
            com = com_ser.save()
        else:
            print(com_ser.errors)

        return Response(b"ok")

class up_down(APIView):
    #jwt
    authentication_classes = [JSONWebTokenAuthentication]
    #登录用户才可以访问
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user_id = request.user.id
        data = request.query_params.dict()
        print(user_id)
        print(data)
        click = int(data['click'])
        print(click)
        da = models.UpAndDown.objects.filter(article=data['art'],user=user_id).first()
        if da:
            if da.is_up:
                print("点赞")
                models.UpAndDown.objects.filter(article=data['art'], user=user_id).delete()
                models.Article.objects.filter(pk=data['art']).update(up_num=F('up_num')-1)
            else:
                print("点踩")
                models.UpAndDown.objects.filter(article=data['art'], user=user_id).delete()
                models.Article.objects.filter(pk=data['art']).update(down_num=F('down_num')-1)
        else:
            if click:
                art = models.Article.objects.filter(id=data['art']).first()
                user = User.objects.filter(id=user_id).first()
                models.UpAndDown.objects.create(article=art, user=user, is_up=True)
                models.Article.objects.filter(pk=data['art']).update(up_num=F('up_num') + 1)
            else:
                art = models.Article.objects.filter(id=data['art']).first()
                user = User.objects.filter(id=user_id).first()
                models.UpAndDown.objects.create(article=art, user=user, is_up=False)
                models.Article.objects.filter(pk=data['art']).update(down_num=F('down_num') + 1)




        return Response('ok')

