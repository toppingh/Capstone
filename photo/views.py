from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Photo
from .serializers import NormalPhotoSerializer, ComplaintPhotoSerializer, EtcPhotoSerializer

# Create your views here.
# 정상 사진 api뷰
class NormalPhotoAPIView(APIView):
    def get(self, request):
        n_photos = Photo.objects.filter(state='GOOD')
        serializer = NormalPhotoSerializer(n_photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 병충해 사진 api뷰
class ComplaintPhotoAPIView(APIView):
    def get(self, request):
        c_photos = Photo.objects.filter(state='BAD')
        serializer = ComplaintPhotoSerializer(c_photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 기타 사진 api뷰
class EtcPhotoAPIView(APIView):
    def get(self, request):
        e_photos = Photo.objects.filter(state='ETC')
        serializer = EtcPhotoSerializer(e_photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)