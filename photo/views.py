import os

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
import requests
from PIL import Image

from .models import Photo
from .serializers import NormalPhotoSerializer, ComplaintPhotoSerializer, EtcPhotoSerializer, AllPhotoSerializer

# Create your views here.
# 정상 사진 api뷰
class NormalPhotoAPIView(APIView):
    def get(self, request):
        n_photos = Photo.objects.filter(state='GOOD')
        serializer = NormalPhotoSerializer(n_photos, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 병충해 사진 api뷰
class ComplaintPhotoAPIView(APIView):
    def get(self, request):
        c_photos = Photo.objects.filter(state='BAD')
        serializer = ComplaintPhotoSerializer(c_photos, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 기타 사진 api뷰
class EtcPhotoAPIView(APIView):
    def get(self, request):
        e_photos = Photo.objects.filter(state='ETC')
        serializer = EtcPhotoSerializer(e_photos, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 전체 사진 api뷰
class AllPhotoAPIView(APIView):
    def get(self, request):
        all_photos = Photo.objects.all()
        serializer = AllPhotoSerializer(all_photos, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# Flask api로 요청 보내기
def send_photo_to_AI(request):
    if request.method == 'POST':
        # 유저 사진
        # if request.FILES.get('file') is not None:
        files = request.FILES.get('file')

        if files:
            img_check = os.path.splitext(files.name)[1].lower()

            if img_check not in ['.png', '.jpg', '.jpeg']:
                img = Image.open(files)
                img = img.convert('RGB')
                img_path = 'image.png'
                img.save(img_path)
                files = open(img_path, 'rb')

            # AI서버의 rest api 주소
            AI_url = 'http://127.0.0.1:5000/detect'

            # 파일과 데이터를 함께 POST 요청 보내기
            files = {'file': files}
            response = requests.post(AI_url, files=files)

            # (임시)이미지 파일 삭제
            if 'img_path' in locals():
                os.remove(img_path)

            # 요청 결과 처리
            if response.status_code == 200:
                # ai 서버에서 넘겨온 이미지 db에 저장
                ai_image = Photo()
                ai_image.image.save('default_image.jpg', ContentFile(response.content))
                ai_image.save()

                # db에 저장된 이미지를 앱으로 response
                db_image = get_object_or_404(Photo, pk=ai_image.pk)
                response = HttpResponse(db_image.image.read(), content_type='image/jpg')
                response['Content-Disposition'] = 'attachment; filename="default_image"'
                return response

            else:
                return HttpResponse({'message': "사진을 보내는데 실패했습니다! 다시 시도해주세요."}, status=response.status_code)
        else:
            return HttpResponse({'message': "사진 파일을 찾을 수 없습니다."}, status=404)

    return HttpResponse({"message": "잘못된 요청입니다!"}, status=405)
