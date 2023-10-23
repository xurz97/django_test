from django.shortcuts import render
from demo import models
from django.shortcuts import redirect
def gohome(request):
    return redirect('/')
# Create your views here.

def g(request):
    g = 'a'
    if request.method == 'POST':
        g = request.POST.get('g')
        return render(request, 'g.html', locals())
    return render(request, 'g.html', locals())

def home(request):
    if request.session.get('id') == None:
        return render(request, 'login.html')
    login_name = ''
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    return render(request, 'home.html', {"name": login_name})




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
                return render(request, 'Login.html', {"message": message})
            if user.password == password:
                request.session['id'] = user.id    # 记录用户已登录
                return redirect('/')
            else:
                message = '密码错误'
                return render(request, 'Login.html', {"message": message})
    return render(request, 'Login.html')


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
            return render(request, 'Register.html', {"message": message})
        user = models.User()
        user.username = username
        user.password = password
        user.save()
        request.session['id'] = user.id   # 记录用户已登录
        return redirect('../')
    return render(request, 'Register.html')


def logout(request):
    request.session.flush()
    return redirect('/')


import os

from django.http import StreamingHttpResponse, Http404
from django.shortcuts import render, redirect

def upload(request):
    if request.method == 'POST':
        file = request.FILES.get("file", None)
        if not file:
            message = "no files for upload!"
            return render(request, 'file.html', locals())
        if not file.name.endswith(".jpg"):              # 检测是否为jpg，防止文件上传攻击
            message = "only JPG is accepted!"
            return render(request, 'file.html', locals())
        file.name = 'pic' + '.jpg'          # 再次改名，防止文件上传攻击
        if os.path.exists(file.name):
            os.remove(file.name)            # 如果存在该文件名的文件则移除
        destination = open(os.path.join("static/file", file.name), 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        message = "upload successfully!"
        return render(request, 'file.html', locals())
    return render(request, 'file.html')


def download(request):
    try:
        response = StreamingHttpResponse(open('static/file/pic.jpg', 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename('static/file/pic.jpg')
        return response
    except Exception:
        raise Http404
    
from django import forms
class DataForm(forms.ModelForm):
    data = forms.CharField( widget=forms.Textarea )
    def save_data(self):
        with open('data.txt', 'w') as f:
            f.write(data)


def work(lines):
    output=""
    for line in lines:
        output+=line.upper()
    return output

def work2(lines):
    output=""
    for line in lines:
        output+=line+'\n'
    return output

def file(request):
    if request.method == 'POST':
        data = request.POST.get('gender')
        with open('./static/InputFile/data.txt', 'w') as f:
           for line in data.splitlines():
                f.write(line.strip() + '\n')
        print("choice: "+data)
        data = request.POST.get('input_data1')
        print("text1: "+data)
        newlines1 = data.splitlines()
        with open('./static/InputFile/data.txt', 'a') as f:
            for line in data.splitlines():
                f.write(line.strip() + '\n')
        data = request.POST.get('input_data2')
        print("text2: "+data)
        newlines2 = data.splitlines()
        with open('./static/InputFile/data.txt', 'a') as f:
            for line in data.splitlines():
                f.write(line.strip() + '\n')
        f = open ('./static/InputFile/data.txt','r')
        lines = f.readlines()
        output = work(lines)
        #message = "upload successfully!"
        newlines1 = work2(newlines1)
        newlines2 = work2(newlines2)
        context = {
            "v": newlines1,
            "w": output,
            "n": newlines2,
            #"message": message
        }
        return render(request, 'file.html',context)
    return render(request, 'file.html')

from .forms import SelectTestForm
def test(request):
    if request.method == 'POST':
        data = request.POST.get('code')
        print(data)
        with open('./static/InputFile/data1.txt', 'w') as f:
           for line in data.splitlines():
            f.write(line.strip() + '\n')
        f = open ('./static/InputFile/data1.txt','r')
        lines = f.readlines()
        newlines = work2(lines)
        output = work(lines)
        #message = "upload successfully!"
        context = {
            "v": newlines,
            "w": output,
         #   "message": message
        }
        return render(request, 'test.html',context)
    return render(request, 'test.html')
