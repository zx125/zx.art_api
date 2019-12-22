from django.urls import path, re_path

from . import views
urlpatterns = [
    path('cat', views.CatListAPIView.as_view()),
    path('cat_data', views.CatDataListAPIView.as_view()),
    path('cat_banner', views.CatBannerListAPIView.as_view()),
    path('car_order', views.PayAPIView.as_view()),
]
