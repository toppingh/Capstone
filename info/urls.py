from django.urls import path
from .views import AllQnaAPIView, QnaAPIView, EditQnaAPIView, ScrapAPIView, AllReportAPIView, ReportAPIView

urlpatterns = [
    path('qna/', AllQnaAPIView.as_view()),
    path('qna/<int:pk>/', QnaAPIView.as_view()),
    path('qna/edit/<int:pk>/', EditQnaAPIView.as_view()),
    path('scrap/', ScrapAPIView.as_view()),
    path('report/', AllReportAPIView.as_view()),
    path('report/<int:pk>/', ReportAPIView.as_view()),
]