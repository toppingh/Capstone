"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token
# from accounts.views import validate_jwt_token

from django.conf.urls.static import static
from project import settings

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('home/', include('home.urls')),
    path('info/', include('info.urls')),
    path('photo/', include('photo.urls')),
    path('a1ds5fa6eragsdfa565awaf3d5a4e/', admin.site.urls),
    # path('validate/', validate_jwt_token),
    # path('verify/', verify_jwt_token),
    # path('refresh/', refresh_jwt_token), accounts.urls로 사용가능
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)