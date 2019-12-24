from rest_framework.serializers import ModelSerializer

from . import models
from django.conf import settings
from libs.iPay import alipay
import time
from libs.iPay import alipay,alipay_gateway
class ClubModelSerializer(ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id','name','province','city', 'area', 'address', 'nums', 'brief','img_url')

class ClubDataSerializer(ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id','name','province','city', 'area', 'address', 'nums', 'brief','img_url','admin','c_time','deta','rule','money')

class OrderModelSerializer(ModelSerializer):

    class Meta:
        model = models.Order
        fields = (
            'club',
        )

    def validate(self, attrs):
        club_id = attrs['club'].id

        car = models.Club.objects.filter(id=club_id).first()

        price = car.detail.spend

        print(price)
        # 生成订单号
        order_on = self._get_order_no()

        # 生成订单链接
        order_params = alipay.api_alipay_trade_page_pay(out_trade_no=order_on,
                                                        total_amount=float(price),
                                                        subject="加入俱乐部",
                                                        return_url=settings.RETURN_URL2,  # 同步回调的前台接口
                                                        notify_url=settings.NOTIFY_URL  # 异步回调的后台接口
                                                        )
        pay_url = alipay_gateway + order_params

        # 将支付链接保存在serializer对象中
        self.pay_url = pay_url

        # 添加额外的订单号字段
        attrs['out_trade_no'] = order_on
        attrs['payed'] = price

        # 视图类给序列化类传参
        attrs['user'] = self.context.get('request').user
        # 代表校验通过
        return attrs

    def _get_order_no(self):
        no = '%s' % time.time()
        return no.replace('.', '', 1)
