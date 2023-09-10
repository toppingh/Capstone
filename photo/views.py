import os

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
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
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'heic']


def file_extension(filename):
    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)


@csrf_exempt
# Flask api로 요청 보내기
def sendAI(request):
    try:
        if request.method == 'POST':
            user_image = request.FILES.get('user_image')
            email = request.POST.get('email')

            if file_extension(user_image.name):
                save_image = photo_save(user_image)

                if save_image:
                    # ai_server = 'http://127.0.0.1:5000/detect/'

                    # data = {'email': email}
                    # files = {'user_image': user_image}
                    # ai_image = requests.post(ai_server, data=data, files=files)  # ai서버로 post
                    #
                    # print(data, files) # 리액트가 보낸 요청 프린트
                    #
                    # if ai_image.status_code == 200: # ai 응답
                    #     return HttpResponse(ai_image.content, content_type='application/json')
                    # else:
                    return JsonResponse('이미지 저장 완료', status=200, safe=False)
                    print(save_image)
                else :
                    return JsonResponse('이미지 저장 실패', status=500, safe=False)
            else :
                return JsonResponse('올바른 이미지 확장자가 아님', status=400, safe=False)

        return JsonResponse('POST 메소드만 요청 가능', status=405, safe=False)

    except Exception as e:
        print(f'예외 발생 : {str(e)}')
        return JsonResponse('서버에서 예외 발생', status=500, safe=False)


# 기존 코드에서 사용했던 photo_save함수
def photo_save(image):
    try:
        image_save = 'media/user_images/'
        os.makedirs(image_save, exist_ok=True)
        filename = os.path.join(image_save, image.name)
        with open(filename, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        return open(filename, 'rb')

    except Exception as e:
        print(f'이미지 저장 중 예외 발생: {str(e)}')
        return None