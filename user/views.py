from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth # 사용자 auth 기능


#HOME
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/')
    else:
        return redirect('/signin')


#로그인
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            return redirect('/')
        else:
            return redirect('/signin')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'login.html')


#회원가입
def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        exist_user = get_user_model().objects.filter(username=username)
        if exist_user:
            return render(request, 'signup.html', {'error': '사용자 이름이 이미 존재합니다.'})
        else:
            UserModel.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/signin')
