import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechat.settings.dev")

django.setup()

from django.conf import settings
from wechat_01 import models,serializers


def get_son(data):
    lis=[]
    for i in data:
        if not i['parent_id']:
            i['level']=0
        lis.append(i)
    return  lis

data = models.Category.objects.filter(is_show=True).order_by("p_order").all()
data=serializers.Category_ser(instance=data,many=True).data
data=get_son(data)

print(data)