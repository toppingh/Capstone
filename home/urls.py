from django.urls import path, include

from .views import *

urlpatterns = [
    path('blight/<int:pk>/', BlightAPIView.as_view()),
    path('blight/', AllBlightAPIView.as_view()),
    path('pest/<int:pk>/', PestAPIView.as_view()),
    path('pest/', AllPestAPIView.as_view()),
    path('history/<int:pk>/', HistoryAPIView.as_view()),
    path('history/', AllHistoryAPIView.as_view()),
    # path('search/', ResultsAPIView.as_view()),
    path('search/', results, name='search_results'),
    path('date-search/', date_results, name='date_results'),
]
