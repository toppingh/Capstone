from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blight, Pest, History
from .serializers import BlightSerializer, PestSerializer, HistorySerializer

# Create your views here.
# 병해 전체 api 뷰
class AllBlightAPIView(APIView):
    def get(self, request):
        blights = Blight.objects.all()
        serializer = BlightSerializer(blights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병해 api 뷰 (상세)
class BlightAPIView(APIView):
    def get(self, request, pk):
        blight = get_object_or_404(Blight, id=pk)
        serializer = BlightSerializer(blight)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병충 전체 api 뷰
class AllPestAPIView(APIView):
    def get(self, request):
        pests = Pest.objects.all()
        serializer = PestSerializer(pests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병충 api 뷰 (상세)
class PestAPIView(APIView):
    def get(self, request, pk):
        pest = get_object_or_404(Pest, id=pk)
        serializer = PestSerializer(pest)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 히스토리 api 뷰 (상세)
class HistoryAPIView(APIView):
    def get(self, request, pk):
        history = get_object_or_404(History, id=pk)
        serializer = HistorySerializer(history)
        return Response(serializer.data, status=status.HTTP_200_OK)