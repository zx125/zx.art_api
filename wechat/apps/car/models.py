from django.db import models

# Create your models here.
from utils.model import BaseModel
from django.conf import settings

class Stock(BaseModel):
    stock_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)#库存量
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name=models.CharField(max_length=20)
    p_order=models.IntegerField(default=0)
    price_cat = models.CharField(default=0,max_length=20,verbose_name="价格区间")
    else_cat = models.CharField(default=0,max_length=20,verbose_name="自定义分类")
    image = models.OneToOneField(to='club.Images', to_field='image_id', on_delete=models.CASCADE, db_constraint=False,null=True)
    def __str__(self):
        return self.category_name

class Order(models.Model):
    status_choices = (("active", '活动订单'), ("dead", '作废订单'), ("finish", '已完成订单'))
    pay_status_choices = ((0, '未付款'), (1, '已付款'))
    ship_status_choices = ((0, '未发货'), (1, '已发货'))

    order_id = models.CharField(max_length=50, unique=True, primary_key=True)
    status = models.CharField(choices=status_choices, default="active", max_length=50)
    pay_status = models.SmallIntegerField(choices=pay_status_choices, default=0)
    #以支付金额
    payed = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    #支付方式
    pay_app = models.CharField(max_length=100)
    user = models.ForeignKey(to="user.User", related_name="Order", db_constraint=False,on_delete=models.CASCADE)
    #数量
    quantity = models.IntegerField(default=0)
    #备忘录
    memo = models.CharField(max_length=200, default=0)
    consignee_name = models.CharField(max_length=200, default=0)
    consignee_area = models.CharField(max_length=200, default=0)
    consignee_address = models.CharField(max_length=200, default=0)
    consignee_zip = models.CharField(max_length=200, default=0)
    consignee_mobile = models.CharField(max_length=200,default=0)

    def __str__(self):
        return self.order_id

class Car_detail(BaseModel):
    environmental_type={
        (0, '国III'),
        (1, '国VI'),
        (2, '国V'),
        (3, '国IV'),
    }
    intor = models.CharField(max_length=500,verbose_name="详细描述")
    environmental = models.SmallIntegerField(choices=environmental_type,verbose_name="环保标准")
    power = models.IntegerField(verbose_name="功率")
    engine = models.CharField(max_length=30,verbose_name="发动机")
    transmission = models.CharField(max_length=30,verbose_name="变速箱")
    structure = models.CharField(max_length=30,verbose_name="几座几门")
    size = models.CharField(max_length=30,verbose_name="长宽高")
    accelerate = models.DecimalField(max_digits=2,decimal_places=2,verbose_name="百公里加速")
    max_speed = models.DecimalField(max_digits=3,decimal_places=2,verbose_name="极限速度")
    oil = models.DecimalField(max_digits=3,decimal_places=2,verbose_name="油耗")
    url = models.CharField(max_length=50,verbose_name="视频链接")
    quality = models.IntegerField("质保/月")
    def __str__(self):
        return self.id

class Car(BaseModel):
    car_type = {
        (0, '商务车'),
        (1, 'SUV'),
        (2, '电动车'),
        (3, '豪华车'),
        (4, '跑车'),
    }
    car_tab = {
        (0, '热门'),
        (1, '限量'),
        (2, '普通'),
        (3, '珍贵'),
    }
    name = models.CharField(max_length=30,verbose_name="车名")
    brand = models.CharField(max_length=30,verbose_name="品牌")
    model = models.CharField(max_length=30,verbose_name="型号")
    type = models.SmallIntegerField(choices=car_type,verbose_name="车辆类型")
    tab = models.SmallIntegerField(choices=car_tab,verbose_name="车辆标签")
    image = models.OneToOneField(to="club.Images",db_constraint=False,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.OneToOneField(to="Stock",db_constraint=False,on_delete=models.DO_NOTHING)
    detail = models.OneToOneField(to="Car_detail",db_constraint=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
