from django.urls import path
from .views import AllBlightAPIView, BlightAPIView, AllPestAPIView, PestAPIView, HistoryAPIView

urlpatterns = [
    path('blight/<int:pk>/', BlightAPIView.as_view()),
    path('blight/', AllBlightAPIView.as_view()),
    path('pest/<int:pk>/', PestAPIView.as_view()),
    path('pest/', AllPestAPIView.as_view()),
    path('histories/<int:pk>/', HistoryAPIView.as_view()),
]