from django.contrib.auth import authenticate, login, logout
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import UserSerializer

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        if request.user.is_authenticated:
            return Response({"status": "already_authenticated."})
        email = request.data.get('email')
        password = request.data.get('password')
        if not email:
            return Response({'error': "'email' field is missing."})
        if not password:
            return Response({'error': "'password' field is missing."})
        user = authenticate(username=email, password=password, request=request)
        if user is not None:
            login(request, user)
            return Response(UserSerializer(user).data)
        else:
            return Response({"status": "login_failed"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'success': 'Loggout out'})
        except Exception as error:
            print(error)
            return Response({'error': 'Something went wrong when logging out.'})

