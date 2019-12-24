from django.shortcuts import render
from . import models,serializers
from utils import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.conf import settings
from utils.response import APIResponse
from rest_framework.generics import ListAPIView

from .paginations import ClubePageNumberPagination

class ClubListAPIView(ListAPIView):
    queryset = models.Club.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.ClubModelSerializer

    # 分页器
    pagination_class = ClubePageNumberPagination

class PayAPIView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = serializers.OrderModelSerializer(data=request.data,context={'request':request})
        # 信息校验
        serializer.is_valid(raise_exception=True)
        # 订单入库
        serializer.save()
        # 返回一个支付链接
        return Response(serializer.pay_url)

class DetailAPIView(APIView):
    def get(self,request,*args,**kwargs):
        data = request.query_params.dict()
        club = models.Club.objects.filter(pk=data['id']).first()
        club_data = serializers.ClubDataSerializer(club).data

        return APIResponse(
            results=club_data
        )

class SuccessAPIView(APIView):
    #jwt
    authentication_classes = [JSONWebTokenAuthentication]
    #登录用户才可以访问
    permission_class = [IsAuthenticated]
    def patch(self,request,*args,**kwargs):
        data = request.query_params.dict()
        order_id = data['out_trade_no']
        order = models.Order.objects.filter(out_trade_no=order_id).first()
        c_id = order.club.id
        print(c_id)
        print(request.user)
        print(request.user.id)
        from user import models as u_mo
        u_mo.User.objects.filter(id=request.user.id).update(club=c_id)
        models.Order.objects.filter(out_trade_no=order_id).update(pay_status=1)
        return Response("ok")



