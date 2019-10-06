from django.shortcuts import render,redirect

from django.http import  HttpResponse,HttpRequest
# Create your views here.

#主页视图函数
def index(request):
    return render(request,'index.html')
#登录函数
def login(request):
    return render(request,'users/login.html')
#注册函数
def register(request):
    return render(request,'users/register.html')

#修改密码函数
def forget(request):
    return render(request,'users/forget.html')