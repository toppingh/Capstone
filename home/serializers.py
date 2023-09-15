from rest_framework import serializers

from .models import *

# 병해 조회
class BlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blight
        fields = ('id', 'name', 'blight_img', 'causation')

# 병충 조회
class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = ('id', 'name', 'pest_img', 'causation')

# 히스토리 조희
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'