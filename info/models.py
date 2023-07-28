from django.db import models
from photo.models import *
from accounts.models import *

# Create your models here.
# 지난기록
class UserHistory(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    result_state = (
        ('GOOD', 'normal'),
        ('BAD', 'complaint'),
        ('ETC', 'etc'),
    )
    state = models.CharField(max_length=20, choices=result_state, default='GOOD', null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at'] # 정렬

    def __str__(self):
        return self.result_state

# 문의
class QnA(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    title = models.CharField(max_length=100) # 문의 제목
    content = models.CharField(max_length=700) # 문의 내용
    imageFiles = models.ImageField(null=True, upload_to='QnA/', blank=True) # 문의 파일 첨부

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬

    def __str__(self):
        return self.title

# 책갈피
class Scrap(models.Model):
    email = models.EmailField()  # 이메일은 필수, 유저 구분용
    scrap_result = (
        ('GOOD', 'normal'),
        ('BAD', 'complaint'),
        ('ETC', 'etc'),
    )
    result = models.CharField(max_length=20, choices=scrap_result, default='GOOD', null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬

    def __str__(self):
        return self.email

# 제보
class Report(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    title = models.CharField(max_length=100) # 제보글 제목
    content = models.CharField(max_length=700) # 제보글 내용
    imageFiles = models.ImageField(null=True, upload_to='reports/', blank=True) # 제보 파일 첨부

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬

    def __str__(self):
        return self.title