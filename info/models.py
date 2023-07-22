from django.db import models
from photo.models import *
from accounts.models import *

# Create your models here.
# 지난기록
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저 불러오기
    infect_history = models.ForeignKey(Infect, on_delete=models.CASCADE) # 병충해 기록
    normal_history = models.ForeignKey(Normal, on_delete=models.CASCADE) # 정상 기록
    date = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        ordering=['date'] # 정렬


# 문의
class QnA(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 문의 작성자
    title = models.CharField(max_length=100) # 문의 제목
    content = models.CharField(max_length=700) # 문의 내용
    imageFiles = models.ImageField(null=True, upload_to='QnA/', blank=True) # 문의 파일 첨부

    def __str__(self):
        return self.author

# 책갈피
class Scrap(models.Model):
    code = models.ForeignKey(Photo.resultCode, on_delete=models.CASCADE) # 기록 코드
    infect_content = models.ForeignKey(Infect, on_delete=models.CASCADE) # 병충해 내용
    date = models.ForeignKey(Photo, on_delete=models.CASCADE) # 날짜

    def __str__(self):
        return self.code

# 제보
class Report(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    title = models.CharField(max_length=100) # 제보글 제목
    content = models.CharField(max_length=700) # 제보글 내용
    imageFiles = models.ImageField(null=True, upload_to='reports/', blank=True) # 제보 파일 첨부

    def __str__(self):
        return self.author

# 재설정
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 재설정은 뷰에서...?