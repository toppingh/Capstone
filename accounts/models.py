from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username :
            raise ValueError("아이디를 입력해야 합니다.")
        if not email :
            raise ValueError("이메일을 입력해야 합니다.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    profileImg = models.ImageField(upload_to='profiles/%Y/%m/%d', default='default.png', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-created_at']
