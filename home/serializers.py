from rest_framework import serializers

from .models import *

# 메인 화면
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('blight_list', 'pest_list', 'history_list', 'created_at')

# 병해 조회
class HomeBlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blight
        fields = ('name', 'blight_img', 'causation')

# 병충 조회
class HomePestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = ('name', 'pest_img', 'causation')

# 히스토리 조희
class HomeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('name', 'history_img')