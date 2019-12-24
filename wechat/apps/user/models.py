from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    club = models.ForeignKey(to="club.Club",related_name="user", db_constraint=False, on_delete=models.DO_NOTHING, default=0)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    class Meta:
        db_table = 'zx_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

