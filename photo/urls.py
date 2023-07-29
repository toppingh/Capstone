from django.urls import path
from .views import NormalPhotoAPIView, ComplaintPhotoAPIView, EtcPhotoAPIView

urlpatterns = [
    path('normal/', NormalPhotoAPIView.as_view()),
    path('complaint/', ComplaintPhotoAPIView.as_view()),
    path('etc/', EtcPhotoAPIView.as_view()),
]