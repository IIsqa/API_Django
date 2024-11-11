# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import RegisterForm, LoginForm


from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
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