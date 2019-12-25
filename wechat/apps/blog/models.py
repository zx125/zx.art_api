from django.db import models
from utils.model import BaseModel
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name



class Article(BaseModel):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    content = models.TextField()  # 大段文本

    # 数据库优化字段(******)
    comment_num = models.BigIntegerField(default=0)
    up_num = models.BigIntegerField(default=0)
    down_num = models.BigIntegerField(default=0)
    user = models.ForeignKey(to='user.User', db_constraint=False,on_delete=models.DO_NOTHING)

    # 外键字段
    tags = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))
    category = models.ForeignKey(to='Category', null=True,db_constraint=False,on_delete=models.DO_NOTHING)

    @property
    def zx_time(self):
        print(type(self.created_time))
        return self.created_time.strftime("%Y-%m-%d %H:%M")

    @property
    def user_ico(self):
        from django.conf import settings
        return f"{settings.IMG_BASE_URL}/{self.user.icon}"


    @property
    def use_name(self):
        return self.user.username
    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article',db_constraint=False,on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(to='Tag',db_constraint=False,on_delete=models.DO_NOTHING)


class UpAndDown(models.Model):
    user = models.ForeignKey(to='user.User',db_constraint=False,on_delete=models.DO_NOTHING)
    article = models.ForeignKey(to='Article',db_constraint=False,on_delete=models.DO_NOTHING)
    is_up = models.BooleanField()  # 传True/False   存1/0


class Comment(models.Model):
    user = models.ForeignKey(to='user.User',db_constraint=False,on_delete=models.DO_NOTHING)
    article = models.ForeignKey(to='Article',db_constraint=False,on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(to='self',related_name="haha",db_constraint=False,on_delete=models.DO_NOTHING)

    @property
    def user_name(self):
        return self.user.username

    # @property
    # def data(self):
    #     temp_com_list = []
    #     for com in self.parent.all():
    #         temp_com_list.append({
    #             'name': com.name,
    #             'sex': com.get_sex_display(),
    #             'mobile': com.detail.mobile
    #         })
    #     return temp_com_list

    @property
    def zx_time(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M")
