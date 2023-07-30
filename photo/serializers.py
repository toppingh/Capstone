from rest_framework import serializers
from .models import *

# 정상 사진
class NormalPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'state', 'explain') # 정상은 이름이 없으니 제외

# 병충해 사진
class ComplaintPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'ai_name', 'state', 'explain')

# 기타 사진
class EtcPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'state', 'explain')

# 전체 사진
class AllPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'ai_name', 'state', 'explain')