from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import requests
from tkinter import Tk, filedialog # 이미지 파일 경로

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

# flask api와 통신
def detect_objects(request):
    flask_api_url = 'http://127.0.0.1:5000/detect' # flask api url
    #django_api_url = 'http://127.0.0.1:8000/photo/all'

    #root = Tk()
    #root.withdraw()
    # 이미지 선택 대화상자 부르기
    image_files_path = filedialog.askopenfilename(title='Images', filetype=[('Image Files', ['.jpg', '.png', '.jpeg', '.gif'])])
    #root.destroy()

    if not image_files_path:
        print('이미지가 선택되지 않았습니다.')
        return

    # flask api에 요청 보내기
    files = {'image':image_files_path}
    response = requests.post(flask_api_url, files=files) # requests로 flask rest api로 전달

    # flask api의 응답을 JSON으로 반환
    if response.status_code == 200:
        result = response.json()
        return JsonResponse(result, status=200)
    else:
        return JsonResponse({'error': 'Flask API와 연결 실패'}, status=500)