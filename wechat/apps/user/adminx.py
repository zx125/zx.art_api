# home/adminx.py
# xadmin全局配置
import xadmin
from xadmin import views
from . import models
# 注册
# xadmin.site.register(models.Banner)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "小猿购车"  # 设置站点标题
    site_footer = "小猿购车有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)
