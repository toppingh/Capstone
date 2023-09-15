import io
import os

from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import requests
import tempfile
import base64
from PIL import Image

from home.models import Blight, History
from project.settings import MEDIA_ROOT, MEDIA_URL
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
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    for chunk in user_image.chunks():
                        temp_file.write(chunk)

                file_name = user_image.name  # 파일 이름 유지
                file_path = os.path.join(f'media/user_images/{str(file_name)}')

                if save_image:
                    ai_server = 'http://172.18.81.248:5000/detect'

                    data = {'email': email}
                    files = {'file': (file_name, open(file_path, 'rb'))}
                    ai_image = requests.post(ai_server, data=data, files=files)  # ai 서버로 post

                    print(data, files) # 리액트가 보낸 요청 프린트

                    if ai_image.status_code == 200: # ai 응답
                        ai_data = ai_image.json()
                        ai_result = ai_data.get('result', {}).get('ai_result', '')  # ai_result 값 추출
                        ai_name = ai_data.get('result', {}).get('ai_name', '')
                        ai_images = ai_data.get('result', {}).get('ai_images', '')

                        try:
                            blight = Blight.objects.get(name=ai_name)
                            explain = blight.causation
                        except Blight.DoesNotExist:
                            explain = '정상 작물입니다.'

                        if ai_images:
                            ai_image_data = ai_images[0]
                            try:
                                image_data = base64.b64decode(ai_image_data)
                                image = Image.open(io.BytesIO(image_data))

                                image_file = InMemoryUploadedFile(
                                    io.BytesIO(image_data),
                                    None,
                                    str(file_name),
                                    'image/jpeg',
                                    len(image_data),
                                    None
                                )

                                image_path = os.path.join(MEDIA_ROOT, 'photos', str(file_name))
                                with open(image_path, 'wb') as dest:
                                    for chunk in image_file.chunks():
                                        dest.write(chunk)

                                photo = Photo(email=email, image=image_path, state=ai_result, name=ai_name, explain=explain)
                                print(email, ai_result, ai_name)
                                photo.save()

                            except Exception as e:
                                print(f'이미지 저장 중 예외 발생: {str(e)}')
                                return HttpResponse('이미지 저장 중 예외 발생', status=500)

                        return HttpResponse(ai_image.content, content_type='application/json')
                        print(ai_image.content)
                    else:
                        return HttpResponse('AI 서버 응답 에러', status=ai_image.status_code)
                else:
                    return HttpResponse('올바른 이미지 확장자가 아님', status=400)

        return HttpResponse('POST 메소드만 요청 가능', status=405)

    except Exception as e:
        print(f'예외 발생 : {str(e)}')
        return HttpResponse('서버에서 예외 발생', status=500)


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
        return HttpResponse('이미지 저장 중 예외 발생', status=500)
