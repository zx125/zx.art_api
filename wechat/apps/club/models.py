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
    creat_user = models.OneToOneField(to="user.User", related_name="club_user", db_constraint=False, on_delete=models.DO_NOTHING,default=1)

    # 简介
    brief = models.TextField(max_length=100)
    image = models.OneToOneField(to='Images', to_field='image_id', on_delete=models.CASCADE, db_constraint=False)
    # 人数
    nums = models.IntegerField()
    detail = models.OneToOneField(to='Detail', on_delete=models.CASCADE, db_constraint=False,default=1)

    @property
    def img_url(self):
        return settings.IMG_BASE_URL+str(self.image.image_url)

    @property
    def admin(self):
        return self.creat_user.username

    @property
    def c_time(self):
        return self.created_time.strftime("%Y-%m-%d %H:%M")

    @property
    def deta(self):
        return self.detail.intor

    @property
    def rule(self):
        return self.detail.rule

    @property
    def money(self):
        return self.detail.spend

    class Meta:
        db_table = 'zx_club'
        verbose_name_plural = '俱乐部表'

    def __str__(self):
        return self.name

class Detail(BaseModel):
    # 详细介绍
    intor = models.TextField(max_length=550)

    rule = models.TextField(max_length=250)

    spend = models.IntegerField()

class Order(BaseModel):
    pay_status_choices = ((0, '未付款'), (1, '已付款'))
    pay_status = models.SmallIntegerField(choices=pay_status_choices, default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")
    club = models.ForeignKey(to="Club",related_name="order",db_constraint=False,on_delete=models.DO_NOTHING)
    # 支付方式
    pay_app = models.CharField(max_length=100)
    payed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.OneToOneField(to="user.User", related_name="order", db_constraint=False, on_delete=models.DO_NOTHING)

