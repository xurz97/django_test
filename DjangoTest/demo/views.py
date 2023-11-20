from django.shortcuts import render
from demo import models
from django.shortcuts import redirect

def login(request):
    if request.session.get('id') != None:  # 只有不在登录状态时才可以进行登录
        return redirect('../')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()            # 除去空格和换行
            password = password.strip()
            try:
                user = models.User.objects.get(username=username)
            except:
                message = '该用户名不存在'
                return render(request, 'login.html', {"message": message})
            if user.password == password:
                request.session['id'] = user.id    # 记录用户已登录
                return redirect('/')
            else:
                message = '密码错误'
                return render(request, 'Login.html', {"message": message})
    return render(request, 'login.html')


def register(request):
    if request.session.get('id') != None:  # 只有不在登录状态时才可以进行注册
        return redirect('../')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = username.strip()  # 除去空格和换行
        password = password.strip()
        if models.User.objects.filter(username=username).exists():
            message = '该用户名已被注册'
            return render(request, 'register.html', {"message": message})
        user = models.User()
        user.username = username
        user.password = password
        user.save()
        request.session['id'] = user.id   # 记录用户已登录
        return redirect('../')
    return render(request, 'register.html')


def logout(request):
    request.session.flush()
    return redirect('/')


import os

from django.http import StreamingHttpResponse, Http404
from django.shortcuts import render, redirect

from .models import MyModel
from . import function
from time import sleep
def diff(request):
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    if request.method == 'POST':
        sleep(5)
        string1 = "差分分析"
        string2 = request.POST.get('blockcipher')
        number1 = request.POST.get('roundmin')
        number2 = request.POST.get('roundmax')
        print(number1)
        print(number2)
        my_model_instance = MyModel(string1=string1, string2=string2)
        my_model_instance.save()
        my_model_instance.result = function.differential(string2,number1,number2)
        my_model_instance.save()
        return render(request, 'history.html', {"name": login_name,'my_model': MyModel.objects.all()})
    return render(request, 'diff.html', {"name": login_name})  
    
def linear(request):
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    if request.method == 'POST':
        sleep(5)
        string1 = "线性分析"
        string2 = request.POST.get('blockcipher')
        number1 = request.POST.get('roundmin')
        number2 = request.POST.get('roundmax')
        my_model_instance = MyModel(string1=string1, string2=string2)
        my_model_instance.save()
        my_model_instance.result = function.linear(string2,number1,number2)
        my_model_instance.save()
        return render(request, 'history.html', {"name": login_name,'my_model': MyModel.objects.all()})
    return render(request, 'linear.html', {"name": login_name})  

def difflinear(request):
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    if request.method == 'POST':
        sleep(5)
        string1 = "差分线性分析"
        string2 = request.POST.get('blockcipher')
        number1 = request.POST.get('roundmin')
        number2 = request.POST.get('roundmax')
        my_model_instance = MyModel(string1=string1, string2=string2)
        my_model_instance.save()
        my_model_instance.result = function.difflinear(string2,number1,number2)
        my_model_instance.save()
        return render(request, 'history.html', {"name": login_name,'my_model': MyModel.objects.all()})
    return render(request, 'difflinear.html', {"name": login_name})  


def history(request):
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    return render(request, 'history.html', {"name": login_name,'my_model': MyModel.objects.all()})

def history_detail_view(request,id):
    # 根据id从数据库中获取记录
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    record = MyModel.objects.all()[id-1]
    # 渲染模板并返回响应
    return render(request, 'history_detail.html', {'name':login_name,'record': record.result})