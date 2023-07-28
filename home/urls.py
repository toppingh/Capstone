from django.urls import path
from .views import HomeAPIView, BlightAPIView, PestAPIView, HistoryAPIView

urlpatterns = [
    path('main/', HomeAPIView.as_view()),
    path('blight/<int:pk>/', BlightAPIView.as_view()),
    path('pest/<int:pk>/', PestAPIView.as_view()),
    path('histories/<int:pk>/', HistoryAPIView.as_view()),
]