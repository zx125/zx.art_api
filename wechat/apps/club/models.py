from django.db import models

# Create your models here.
from utils.model import BaseModel
from django.conf import settings

class Images(models.Model):
    image_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="0")
    image_url=models.ImageField(upload_to='all')
    def __str__(self):
        return self.name

class Club(BaseModel):
    name = models.CharField(max_length=64)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # 详细介绍
    intor = models.TextField(max_length=250)
    # 简介
    brief = models.TextField(max_length=100)
    image = models.OneToOneField(to='Images', to_field='image_id', on_delete=models.CASCADE, db_constraint=False)
    # 人数
    nums = models.IntegerField()

    @property
    def img_url(self):
        return settings.IMG_BASE_URL+str(self.image.image_url)

    class Meta:
        db_table = 'zx_club'
        verbose_name_plural = '俱乐部表'

    def __str__(self):
        return self.name

