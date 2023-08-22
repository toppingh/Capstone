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

# 파일 확장자 구분
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

def file_extension(filename):
    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)

# Flask api로 요청 보내기
def sendAI(request):
    response = None

    if request.method == 'POST':
        # 유저가 보내는 이미지
        user_image_a = request.FILES.get('user_image_a')
        user_image_b = request.FILES.get('user_image_b')

        # AI가 보내는 이미지
        ai_image_a = request.FILES.get('ai_image_a')
        ai_image_b = request.FILES.get('ai_image_b')

        # 이메일
        email = request.POST.get('email')

        # 유저와 ai가 보낸 이미지 구분
        if user_image_a and ai_image_a:
            photo_state = request.POST.get('photo_state')
            if photo_state == 'GOOD':
                if file_extension(user_image_a.name) and file_extension(ai_image_a.name):
                    response = photo_save(photo_state, user_image_a, ai_image_a, email)
            elif photo_state == 'BAD':
                if file_extension(user_image_a.name) and file_extension(ai_image_a.name):
                    response = photo_save(photo_state, user_image_a, ai_image_a, email)
            elif photo_state =='ETC':
                if file_extension(user_image_a.name) and file_extension(ai_image_a.name):
                    response = photo_save(photo_state, user_image_a, ai_image_a, email)

            return HttpResponse(ai_image_a.read(), content_type='image/jpg')

        if user_image_b and ai_image_b:
            photo_state = request.POST.get('photo_state')
            if photo_state == 'GOOD':
                if file_extension(user_image_b.name) and file_extension(ai_image_b.name):
                    response = photo_save(photo_state, user_image_b, ai_image_b, email)
            elif photo_state == 'BAD':
                if file_extension(user_image_b.name) and file_extension(ai_image_b.name):
                    response = photo_save(photo_state, user_image_b, ai_image_b, email)
            elif photo_state == 'ETC':
                if file_extension(user_image_b.name) and file_extension(ai_image_b.name):
                    response = photo_save(photo_state, user_image_b, ai_image_b, email)

            return HttpResponse(ai_image_b.read(), content_type='image/jpg')

        if response is not None:
            return response

        return HttpResponse('이미지 처리 중 오류가 발생했습니다.', status=500)

    return HttpResponse('POST 메소드로만 요청이 가능합니다.', status=405)

# 위에서 사용하는 photo_save함수
def photo_save(photo_state, user_image, ai_image, email):
    # flask api로 요청 전송
    load = {'email':email}
    files = {'user_image':user_image, 'ai_image':ai_image}
    response = requests.post('http://127.0.0.1:5000/detect', data=load, files=files)

    # 이미지 결과를 디비에 저장
    image_result = Photo()
    image_result.photo_state = photo_state

    # 파일명 설정
    if photo_state == 'GOOD':
        filename = 'normal_image.jpg'
    elif photo_state == 'BAD':
        filename = 'complaint_image.jpg'
    else:
        filename = 'etc_image.jpg'

    photo_save(filename, ContentFile(response.content), save=True)
