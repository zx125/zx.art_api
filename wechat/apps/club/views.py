from django.shortcuts import render
from . import models,serializers
# Create your views here.
from django.conf import settings
from rest_framework.generics import ListAPIView

class ClubListAPIView(ListAPIView):
    queryset = models.Club.objects.filter(is_delete=False, is_show=True)[:3]
    serializer_class = serializers.ClubModelSerializer
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return response

