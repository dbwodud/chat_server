from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm,LoginForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

# 메인 화면
def index(request):
    return render(request,'user/index.html')


# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect('/chat/')
    else: 
        form = UserForm()
        return render(request,'user/join.html',{'form':form})

# 로그인
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else: 
        form = LoginForm()
        return render(request,'user/login.html',{'form':form})

# 로그아웃
def logout(request):
    logout(request)
    redirect('/user/login/')
