from django.db import models

# Create your models here.
# 자주 발병하는 병해
class Blight(models.Model):
    name = models.CharField(max_length=20)
    blight_img = models.ImageField(upload_to='blights/%Y/%m/%d', default='default.png')
    causation = models.TextField()
    blight_type = (
        ('DOT', 'CMV'), # 반점
        ('SLIM', 'TMV'), # 얇아짐
        ('STRIPE', 'ToMV'), # 줄무늬

    )

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'blight'
        verbose_name = plural = 'blights'

    def __str__(self):
        return self.name

# 자주 발병하는 병충
class Pest(models.Model):
    name = models.CharField(max_length=20)
    pest_img = models.ImageField(upload_to='pests/%Y/%m/%d', default='default.png')
    causation = models.TextField()

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'pest'
        verbose_name_plural = 'pests'

    def __str__(self):
        return self.name

# 나의 지난 기록
class History(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=20)
    history_img = models.ImageField(upload_to='histories/%Y/%m/%d', default='default.png')
    causation = models.TextField()

    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'history'
        verbose_name_plural = 'histories'

    def __str__(self):
        return self.name