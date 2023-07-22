from django.db import models
from accounts.models import User

# Create your models here.
# 사진
class Photo(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    image = models.ImageField(upload_to='photos/') # 필수
    photo_state = (
        ('GOOD', 'normal'),
        ('BAD', 'complaint'),
        ('ETC', 'etc'),
    )
    name = models.CharField(max_length=60) # 필수
    ai_name = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=20, choices=photo_state, default='GOOD', null=True, blank=True)
    explain = models.CharField(max_length=60, null=True, blank=True) # 이미지에 대한 결과 코멘트
    created_at = models.DateTimeField(auto_now_add=True) # 필수

    def __str__(self):
        return self.name