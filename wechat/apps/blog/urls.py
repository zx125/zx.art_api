from django.urls import path, re_path

from . import views
urlpatterns = [
    path('art', views.ArtListAPIView.as_view()),
    path('art_cat', views.ArtCatListAPIView.as_view()),
    path('art_tab', views.ArtTabListAPIView.as_view()),
    path('art_detail', views.ArtDetailListAPIView.as_view()),

]
