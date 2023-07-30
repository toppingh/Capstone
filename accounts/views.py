from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserProfileSerializer
from .models import User


class UserProfileAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserProfileSerializer(user)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
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
