from datetime import datetime
import json
from django.db import models
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models.functions import ExtractDay, Extract, TruncDate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Blight, Pest, History
from .serializers import BlightSerializer, PestSerializer, HistorySerializer

# Create your views here.
# 병해 전체 api 뷰
class AllBlightAPIView(APIView):
    def get(self, request):
        blights = Blight.objects.all()
        serializer = BlightSerializer(blights, many=True)
        result = {
            "code": "200",
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 병해 api 뷰 (상세)
class BlightAPIView(APIView):
    def get(self, request, pk):
        blight = get_object_or_404(Blight, id=pk)
        serializer = BlightSerializer(blight)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 병충 전체 api 뷰
class AllPestAPIView(APIView):
    def get(self, request):
        pests = Pest.objects.all()
        serializer = PestSerializer(pests, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 병충 api 뷰 (상세)
class PestAPIView(APIView):
    def get(self, request, pk):
        pest = get_object_or_404(Pest, id=pk)
        serializer = PestSerializer(pest)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 히스토리 전체 api 뷰
class AllHistoryAPIView(APIView):
    def get(self, request):
        email = request.user.email
        user_history = History.objects.filter(email=email)

        serializer = HistorySerializer(user_history, many=True)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 히스토리 api 뷰 (상세)
class HistoryAPIView(APIView):
    def get(self, request, pk):
        history = get_object_or_404(History, id=pk)
        serializer = HistorySerializer(history)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return Response(result, status=status.HTTP_200_OK)

# 검색
@csrf_exempt
def results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('q')
        user_email = request.user.email

        if query:
            results = History.objects.filter(email=user_email, name__icontains=query).order_by('-created_at')
            data = {'results': [{'email': result.email, 'name': result.name, 'history_img': result.history_img.url, 'causation': result.causation, 'created_at': result.created_at} for result in results]}
        else:
            data = {'message': '검색어를 입력하시오'}

        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'POST요청 필요'}, status=400)

# 날짜로 검색
@csrf_exempt
def date_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_date = data.get('selected_date')

        if selected_date:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

            user_email = request.user.email

            selected_date_str = selected_date.strftime("%Y-%m-%d")
            results = History.objects.filter(
                created_at__startswith=selected_date_str,  # 날짜 부분만 비교
                email=user_email
            ).order_by('-created_at')

            if results.exists():
                data = {'results': [{'email': result.email, 'name': result.name, 'history_img': result.history_img.url,
                                     'causation': result.causation, 'created_at': result.created_at} for result in
                                    results]}
            else:
                data = {'message': '해당 날짜에 맞는 내역이 없습니다.'}
        else:
            data = {'message': '날짜를 선택하시오'}

        print("selected_date: ", selected_date)
        print("email: ", user_email)
        print("results: ", results)

        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'POST요청 필요'}, status=400)