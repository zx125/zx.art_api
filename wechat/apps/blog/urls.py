from django.urls import path, re_path

from . import views
urlpatterns = [
    path('art', views.ArtListAPIView.as_view()),
    path('art_cat', views.ArtCatListAPIView.as_view()),
    path('art_tab', views.ArtTabListAPIView.as_view()),
    re_path('^art_detail/(?P<pk>\d+)$', views.ArtDetailListAPIView.as_view()),
    path('art_comment', views.ArtComListAPIView.as_view()),
    path('up_down', views.up_down.as_view()),
]
