from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('search', HistoryViewSet)

urlpatterns = [
    path('blight/<int:pk>/', BlightAPIView.as_view()),
    path('blight/', AllBlightAPIView.as_view()),
    path('pest/<int:pk>/', PestAPIView.as_view()),
    path('pest/', AllPestAPIView.as_view()),
    path('history/<int:pk>/', HistoryAPIView.as_view()),
    path('history/', AllHistoryAPIView.as_view()),
]
urlpatterns += router.urls