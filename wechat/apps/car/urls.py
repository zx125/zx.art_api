from django.urls import path, re_path

from . import views
urlpatterns = [
    path('cat', views.CatListAPIView.as_view()),
]
