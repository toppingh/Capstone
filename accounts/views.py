import json
import random
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail import BadHeaderError, send_mail

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

class ChangeProfileImg(APIView):
    def put(self, request, pk):
        user = get_object_or_404(Account, id=pk)
        new_profileImg = request.data.get('profileImg')

        if not new_profileImg:
            return Response({'error': '이미지가 없습니다'}, status=status.HTTP_400_BAD_REQUEST)
        user.profileImg = new_profileImg
        user.save()

        return Response({'message': '프로필 사진이 성공적으로 변경되었습니다!'}, status=status.HTTP_200_OK)

# 비밀번호 재설정을 위한 이메일 전송 (인증 번호 전송)
@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_email = data.get('email')
        print(f"이메일: {user_email}")

        try:
            if Account.objects.filter(email=user_email).exists():
                auth_code = str(random.randint(100000, 999999))
                user_account = Account.objects.get(email=user_email)
                user_account.auth_code = auth_code
                user_account.save()
                print(auth_code)

                subject = '그린단 비밀번호 재설정 안내'
                message = f'비밀번호 재설정을 위한 인증코드를 보내드립니다. 인증 코드 : {auth_code}'
                from_email = 'h62638901@gmail.com'
                recipient_list = [user_email]

                send_mail(subject, message, from_email, recipient_list)

                return JsonResponse({'message': '이메일이 전송되었습니다.'})

            else:
                return JsonResponse({'message': '해당 이메일을 찾을 수 없습니다.'})
        except BadHeaderError:
            return JsonResponse({'message': '유효하지 않은 헤더가 포함되었습니다.'})
        except Exception as e:
            return JsonResponse({'message': str(e)})
    else:
        return HttpResponse(status=405)


@csrf_exempt
def check_auth_code(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_email = data.get('email')
        auth_code = data.get('auth_code')

        try:
            # 데이터베이스에서 해당 이메일에 대한 계정을 가져옵니다.
            user_account = Account.objects.filter(email=user_email).first()

            if user_account:
                db_auth_code = user_account.auth_code
                print('auth_code:', str(auth_code))
                print('db:', str(db_auth_code))
                print(str(db_auth_code) == str(auth_code))

                if db_auth_code == auth_code:
                    return JsonResponse({'message': '비밀번호 재설정 가능', 'status': 200}, status=200)
                else:
                    return JsonResponse({'message': '인증코드가 일치하지 않습니다.'}, status=400)
            else:
                return JsonResponse({'message': '해당 이메일을 찾을 수 없습니다.'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)})
    else:
        return HttpResponse(status=405)
