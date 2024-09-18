from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
from allauth.socialaccount.models import SocialToken

def get_social_token(user):
    token = SocialToken.objects.get_or_create(account__user=user, account__provider='google')
    if token:
        return token.token
    return None

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            print(user,token)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)