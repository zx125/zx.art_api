from django.urls import path, re_path

from . import views
urlpatterns = [
    path('clubs', views.ClubListAPIView.as_view()),
    path('club_order', views.PayAPIView.as_view()),
    path('detail', views.DetailAPIView.as_view()),
    path('success', views.SuccessAPIView.as_view()),
]
