from rest_framework import serializers

from .models import *

# 문의 시리얼라이저
class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = ('email', 'title', 'content', 'qnaImg')

# 스크랩 시리얼라이저
class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ('email', 'result')

# 제보 시리얼라이저
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('email', 'title', 'content', 'reportImg')