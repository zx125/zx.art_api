from rest_framework.serializers import ModelSerializer

from . import models

class ClubModelSerializer(ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('name','province','city', 'area', 'address', 'nums', 'brief','img_url')
