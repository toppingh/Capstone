from rest_framework import serializers

from .models import *

# 문의 시리얼라이저
class QnASerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = QnA
        fields = ('id', 'email', 'title', 'content', 'qnaImg', 'created_at')

# 스크랩 시리얼라이저
class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ('id', 'email', 'result')

# 제보 시리얼라이저
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'email', 'title', 'content', 'reportImg')