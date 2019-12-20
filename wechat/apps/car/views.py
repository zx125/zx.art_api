from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models
from . import serializers
# Create your views here.

class CatListAPIView(ListAPIView):
    queryset = models.Category.objects.filter().order_by('-p_order').all()
    serializer_class = serializers.CatModelSerializer
