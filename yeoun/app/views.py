from django.shortcuts import render, redirect
from .models import Community, Comments, Option
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .utils import upload_and_save

# Create your views here.

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = 'Incorrect ID or Password'
            return render(request, 'common/login.html', {'error': error})
            
        auth.login(request, found_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/option'))
    return render(request, 'common/login.html')

def start(request):
    return render(request, 'common/start.html')

def registration(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        if len(found_user) > 0:
            error = '이미 존재하는 아이디입니다'
            return render(request, 'common/registration.html', {'error' : error})
        
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    return render(request, 'common/registration.html')

def index(request):
    return render(request, 'index.html')

def option(request):
    if request.method == 'POST':
        Option.objects.create(
            option1 = request.POST['option1'],
            option2 = request.POST['option2'],
            user = request.user,
        )
        return redirect('index')
    return render(request, 'common/option.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('index')

def com_list(request):
    posts = Community.objects.all()
    return render(request, 'com_list.html', { 'posts' : posts })

def com_detail(request, key):
    post = Community.objects.get(pk = key)

    if request.method == "POST":
        Comments.objects.create(
            post = post,
            comment = request.POST['comment'],
            author = request.user
        )
        print(option)
        return redirect('com_detail', key)
    return render(request, 'com_detail.html', {'post' : post})

@login_required(login_url = '/common/registration')
def com_new(request):
    if request.method == 'POST':
        file_to_upload = request.FILES.get('img')
        new_post = Community.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            img = upload_and_save(request, file_to_upload)
        )
        return redirect('detail', new_post.pk)
    return render(request, 'com_new.html')

def mypage(request, mykey):
    mystyle = Option.objects.get(user = request.user)
    posts = Community.objects.filter(author = request.user)
    if request.method == 'POST':
        Option.objects.filter(user = request.user).update(
            option1 = request.POST['option1'],
            option2 = request.POST['option2'],
        )
        return redirect('mypage')
    return render(request, 'mypage.html', {'mystyle' : mystyle , 'posts':posts} )


