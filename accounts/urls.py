from django.urls import path, include
from .views import UserProfileAPIView, ChangeUsername, get_csrf_token, ChangeProfileImg, validate_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='get_profile'),
    path('change/profile/', ChangeProfileImg.as_view(), name='profile'),
    path('change/username/', ChangeUsername.as_view(), name='change_username'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('token/', validate_jwt_token, name='jwt_token'),
]