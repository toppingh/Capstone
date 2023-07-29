from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import QnA, Scrap, Report
from .serializers import QnASerializer, ScrapSerializer, ReportSerializer

# Create your views here.
# QnA 뷰 (전체)
class AllQnaAPIView(APIView):
    def get(self, request):
        qnas = QnA.objects.all()
        serializer = QnASerializer(qnas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# QnA 뷰 (상세)
class QnaAPIView(APIView):
    def get(self, request, pk):
        qna = get_object_or_404(QnA, id=pk)
        serializer = QnASerializer(qna)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QnASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        qna = get_object_or_404(QnA, id=pk)
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

# 제보 뷰 (전체)
class AllReportAPIView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 제보 뷰 (상세)
class ReportAPIView(APIView):
    def get(self, request, pk):
        report = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        report = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(report, data=request.data)
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


