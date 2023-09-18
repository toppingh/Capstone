from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail.message import EmailMessage

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

# 이메일
def send_email(request):
    subject = "message" # 타이틀
    to = ["h62638901@gmail.com"]
    from_email = "Greendan@gmail.com"
    message = "주겨달라!!!!!!!!!!!!!"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()

# class SendEmailAPIView(APIView):
#     def post(self, request, format=None):
#         to_email = request.data.get('email') # 리액트에서 email로
#
#         if to_email:
#             try:
#                 send_email('이메일 제목 : 그린단 비밀번호 재설정 안내', '보내는 이메일 주소', [to_email])
#                 return Response({'message': '이메일이 성공적으로 전송되었습니다.'}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response({'message': '이메일 전송 실패: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)