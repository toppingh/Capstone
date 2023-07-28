from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import QnA, Scrap, Report
from .serializers import QnASerializer, ScrapSerializer, ReportSerializer

# Create your views here.
# QnA 뷰
class QnaAPIView(APIView):
    def get(self, request, pk):
        qnas = get_object_or_404(QnA, id=pk)
        serializer = QnASerializer(qnas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QnASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        qnas = get_object_or_404(QnA, id=pk)
        serializer = QnASerializer(QnA, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 스크랩 뷰
class ScrapAPIView(APIView):
    def get(self, request):
        scraps = Scrap.objects.all()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 제보 뷰
class ReportAPIView(APIView):
    def get(self, request, pk):
        reports = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        reports = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(Report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


