from django.urls import path
from .views import AllBlightAPIView, BlightAPIView, PestAPIView, HistoryAPIView

urlpatterns = [
    path('blight/<int:pk>/', BlightAPIView.as_view()),
    path('pest/', AllBlightAPIView.as_view()),
    path('pest/<int:pk>/', PestAPIView.as_view()),
    path('histories/<int:pk>/', HistoryAPIView.as_view()),
]