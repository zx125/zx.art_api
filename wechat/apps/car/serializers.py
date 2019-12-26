from rest_framework.serializers import ModelSerializer
import time
from django.conf import settings
from libs.iPay import alipay,alipay_gateway

from . import models

class CatModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('category_name','id')

class CarModelSerializer(ModelSerializer):
    class Meta:
        model = models.Car
        fields = ('id','name','brand','price','car_type','ima_url')

class CarBannerModelSerializer(ModelSerializer):
    class Meta:
        model = models.Car
        fields = ('id','ima_url')

class OrderModelSerializer(ModelSerializer):

    class Meta:
        model = models.Order
        fields = (
            'car',
        )

    def validate(self, attrs):
        car_id = attrs['car'].id

        car = models.Car.objects.filter(id=car_id).first()

        price = car.price

        print(price)
        # 生成订单号
        order_on = self._get_order_no()

        # 生成订单链接
        order_params = alipay.api_alipay_trade_page_pay(out_trade_no=order_on,
                                                        total_amount=float(price*10000),
                                                        subject="购车",
                                                        return_url=settings.RETURN_URL,  # 同步回调的前台接口
                                                        notify_url=settings.NOTIFY_URL  # 异步回调的后台接口
                                                        )
        pay_url = alipay_gateway + order_params

        # 将支付链接保存在serializer对象中
        self.pay_url = pay_url

        # 添加额外的订单号字段
        attrs['out_trade_no'] = order_on

        # 视图类给序列化类传参
        print(self.context.get('request').user)
        attrs['user'] = self.context.get('request').user
        # 代表校验通过
        return attrs

    def _get_order_no(self):
        no = '%s' % time.time()
        return no.replace('.', '', 1)
