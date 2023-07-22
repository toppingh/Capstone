from django.db import models

# Create your models here.
# 사진
class Photo(models.Model):
    resultCode = models.CharField(max_length=1)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# 정상
class Normal(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='normal_photos')
    content = models.TextField(blank=True)
    img = models.ImageField(upload_to='normal_photos/')

# 병충해
class Infect(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='infect_photos')
    content = models.TextField(blank=True)
    img = models.ImageField(upload_to='infect_photos/')