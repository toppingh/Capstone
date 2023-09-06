from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import UserProfileSerializer
from .models import Account

@api_view(['GET'])
def validate_jwt_token(request):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        data = {'token': token.split()[1]}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
    except Exception as e:
        return Response(e)

    return Response(status=status.HTTP_200_OK)

class UserProfileAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(Account, id=pk)
        serializer = UserProfileSerializer(user)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(Account, id=pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {
                "code": 200,
                "message": "성공적으로 수행됐습니다!",
                "result": serializer.data
            }
            return Response(result, status=status.HTTP_200_OK)
        result = {
            "code": 400,
            "message": "요청에 실패했습니다.",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

class ChangeUsername(APIView):
    def put(self, request):
        user = request.user
        new_username = request.data.get('newUsername')

        if not new_username:
            return Response({'error': '새로운 이름을 입력하세요!'}, status=status.HTTP_400_BAD_REQUEST)
        user.username = new_username
        user.save()

        return Response({'message': '이름이 성공적으로 변경되었습니다!'}, status=status.HTTP_200_OK)


class ChangeProfileImg(APIView):
    def put(self, request, pk):
        user = get_object_or_404(Account, id=pk)
        new_profileImg = request.data.get('profileImg')

        if not new_profileImg:
            return Response({'error': '이미지가 없습니다'}, status=status.HTTP_400_BAD_REQUEST)
        user.profileImg = new_profileImg
        user.save()

        return Response({'message': '프로필 사진이 성공적으로 변경되었습니다!'}, status=status.HTTP_200_OK)