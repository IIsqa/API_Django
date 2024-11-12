# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import RegisterForm, LoginForm


from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenobtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenobtainPairSerializer

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Kullanıcıyı kaydet
            return redirect('login')  # Kayıt sonrası login sayfasına yönlendir
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')  # Giriş yaptıktan sonra yönlendirilecek sayfa
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

