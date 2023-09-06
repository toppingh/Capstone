from django.db import models
# from accounts.models import *

# Create your models here.
# 문의
class QnA(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    title = models.CharField(max_length=100) # 문의 제목
    content = models.CharField(max_length=700) # 문의 내용
    qnaImg = models.ImageField(null=True, upload_to='QnA/', blank=True) # 문의 파일 첨부

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬
        verbose_name = 'ask'
        verbose_name_plural = 'Asks'

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

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬
        verbose_name = 'scrap'
        verbose_name_plural = 'Scraps'

    def __str__(self):
        return self.email

# 제보
class Report(models.Model):
    email = models.EmailField() # 이메일은 필수, 유저 구분용
    title = models.CharField(max_length=100) # 제보글 제목
    content = models.CharField(max_length=700) # 제보글 내용
    reportImg = models.ImageField(null=True, upload_to='reports/', blank=True) # 제보 파일 첨부

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 정렬
        verbose_name = 'report'
        verbose_name_plural = 'reports'

    def __str__(self):
        return self.title