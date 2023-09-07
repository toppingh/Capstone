from django.urls import path
from .views import NormalPhotoAPIView, ComplaintPhotoAPIView, EtcPhotoAPIView, AllPhotoAPIView, sendAI

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('normal/', NormalPhotoAPIView.as_view()),
    path('complaint/', ComplaintPhotoAPIView.as_view()),
    path('etc/', EtcPhotoAPIView.as_view()),
    path('all/', AllPhotoAPIView.as_view()),
    path('test/', sendAI, name='sendAI'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)