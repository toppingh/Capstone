from django.urls import path
from .views import NormalPhotoAPIView, ComplaintPhotoAPIView, EtcPhotoAPIView, AllPhotoAPIView, detect_objects

urlpatterns = [
    path('normal/', NormalPhotoAPIView.as_view()),
    path('complaint/', ComplaintPhotoAPIView.as_view()),
    path('etc/', EtcPhotoAPIView.as_view()),
    path('all/', AllPhotoAPIView.as_view()),
    path('detect/', detect_objects, name='detect'),
]