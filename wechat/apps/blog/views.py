from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from . import serializers
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

class ArtCatListAPIView(ListAPIView):
    queryset = models.Category.objects.filter().all()
    serializer_class = serializers.ArtCatModelSerializer

class ArtTabListAPIView(ListAPIView):
    queryset = models.Tag.objects.filter().all()
    serializer_class = serializers.ArtTabModelSerializer
