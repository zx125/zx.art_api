from django.shortcuts import render
from . import models,serializers
from utils import response
# Create your views here.
from django.conf import settings
from rest_framework.generics import ListAPIView
from .paginations import ClubePageNumberPagination

class ClubListAPIView(ListAPIView):
    queryset = models.Club.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.ClubModelSerializer

    # 分页器
    pagination_class = ClubePageNumberPagination



