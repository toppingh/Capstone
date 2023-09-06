from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import UserProfileAPIView, ChangeUsername, get_csrf_token, ChangeProfileImg, validate_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='get_profile'),
    path('change/profile/<int:pk>/', ChangeProfileImg.as_view(), name='profile'),
    # path('change/username/', ChangeUsername.as_view(), name='change_username'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('token/', validate_jwt_token, name='jwt_token'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/uid-<int:uid>&token=<str:token>>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',)
]