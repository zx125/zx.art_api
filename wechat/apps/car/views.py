from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models
from rest_framework.response import Response
from . import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utils.response import APIResponse
# Create your views here.

class CatListAPIView(ListAPIView):
    queryset = models.Category.objects.filter().order_by('-p_order').all()
    serializer_class = serializers.CatModelSerializer

class CatDataListAPIView(APIView):
    def get(self,request,*args,**kwargs):
        data = request.query_params.dict()
        cat = models.Category.objects.filter(pk=data['qid']).first()
        fen = cat.price_cat
        if fen != "0":
            price = fen.split(",")
            min = int(price[0])
            max = int(price[1])
            cars = models.Car.objects.filter(price__gte=min,price__lt=max).all()
            car_data = serializers.CarModelSerializer(cars,many=True).data
            # print(car_data)
            # print(type(car_data))
            return APIResponse(
                results = car_data
            )
        # print(cat.else_cat)
        return APIResponse()

class CatBannerListAPIView(ListAPIView):
    queryset = models.Car.objects.filter().all()[:3]
    serializer_class = serializers.CarBannerModelSerializer

class CarOrderBannerListAPIView(APIView):
    #jwt
    authentication_classes = [JSONWebTokenAuthentication]
    #登录用户才可以访问
    permission_class = [IsAuthenticated]

class PayAPIView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = serializers.OrderModelSerializer(data=request.data,context={'request':request})
        # 信息校验
        serializer.is_valid(raise_exception=True)
        # 订单入库
        serializer.save()
        # 返回一个支付链接
        return Response(serializer.pay_url)
