from accounts.serializers import UserProfileSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserProfileSerializer(user, context={'request': request}).data
    }