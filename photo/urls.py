from django.urls import path
from .views import NormalPhotoAPIView, ComplaintPhotoAPIView, EtcPhotoAPIView, AllPhotoAPIView, send_photo_to_AI

urlpatterns = [
    path('normal/', NormalPhotoAPIView.as_view()),
    path('complaint/', ComplaintPhotoAPIView.as_view()),
    path('etc/', EtcPhotoAPIView.as_view()),
    path('all/', AllPhotoAPIView.as_view()),
    path('send_photo_to_AI/', send_photo_to_AI, name='to_AI'),
]