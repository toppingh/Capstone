from django.db import models

# Create your models here.
# 자주 발병하는 병해
from django.utils import timezone


class Blight(models.Model):
    name = models.CharField(max_length=20)
    blight_img = models.ImageField(upload_to='blights/%Y/%m/%d', default='default.png')
    causation = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

# 자주 발병하는 병충
class Pest(models.Model):
    name = models.CharField(max_length=20)
    pest_img = models.ImageField(upload_to='pests/%Y/%m/%d', default='default.png')
    causation = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

# 나의 지난 기록
class History(models.Model):
    name = models.CharField(max_length=20)
    history_img = models.ImageField(upload_to='histories/%Y/%m/%d', default='default.png')