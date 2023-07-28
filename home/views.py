from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blight, Pest, History, Home
from .serializers import HomeSerializer, HomeBlightSerializer, HomePestSerializer, HomeHistorySerializer

# Create your views here.
# 메인 화면 뷰
class HomeAPIView(APIView):
    def get(self, request):
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병해 api 뷰 (상세)
class BlightAPIView(APIView):
    def get(self, request, pk):
        blight = get_object_or_404(Blight, id=pk)
        serializer = HomeBlightSerializer(blight)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병충 api 뷰 (상세)
class PestAPIView(APIView):
    def get(self, request, pk):
        pest = get_object_or_404(Pest, id=pk)
        serializer = HomePestSerializer(pest)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 히스토리 api 뷰 (상세)
class HistoryAPIView(APIView):
    def get(self, request, pk):
        history = get_object_or_404(History, id=pk)
        serializer = HomeHistorySerializer(history)
        return Response(serializer.data, status=status.HTTP_200_OK)