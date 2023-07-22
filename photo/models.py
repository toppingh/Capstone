from django.db import models
from accounts.models import User

# Create your models here.
# 사진
class Photo(models.Model):
    email = models.ForeignKey(User.email, blank=False) # 이메일은 필수, 유저 구분용
    image = models.ImageField(upload_to='photos/')
    state = (
        ('0', '정상'),
        ('B', '토마토 잎 곰팡이병'),
        ('C', '토마토 황화 잎말이 바이러스'),
    )
    name = models.CharField(max_length=1, choices=state)
    explain = models.CharField(max_length=100) # 이미지에 대한 결과 코멘트
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name