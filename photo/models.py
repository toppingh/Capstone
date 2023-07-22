from django.db import models
from accounts.models import User

# Create your models here.
# 사진
class Photo(models.Model):
    email = models.EmailField(blank=False) # 이메일은 필수, 유저 구분용
    image = models.ImageField(upload_to='photos/')
    photo_state = (
        ('GOOD', 'normal'),
        ('BAD', 'complaint'),
        ('ETC', 'etc'),
    )
    name = models.CharField(max_length=60)
    ai_name = models.CharField(max_length=60)
    state = models.CharField(max_length=20, choices=photo_state)
    explain = models.CharField(max_length=60) # 이미지에 대한 결과 코멘트
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name