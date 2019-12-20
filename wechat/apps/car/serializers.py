from rest_framework.serializers import ModelSerializer

from . import models

class CatModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('category_name','id')

