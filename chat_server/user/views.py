from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login , authenticate
# Create your views here.

# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect('index')
    else: 
        form = UserForm()
        return render(request,'user/join.html',{'form':form})

# 로그인
def signin(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else: 
        form = UserForm()
        return render(request,'user/login.html',{'form':form})