from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout

def open_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_view_url')
    return render(request, 'open.html')


def ac_create_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_view_url')
    return render(request, 'open.html')



def error_view(request):
    ctx = {

    }
    return render(request, '404.html', ctx)

def my_account_view(request):
    ctx = {

    }
    return render(request, 'my-user-page.html', ctx)
def index_view(request):
    latestpost = Post.objects.filter(category_id=1)
    bisness = Post.objects.filter(category_id=2)
    print(bisness)
    context = {
        'new': NewsItem.objects.all().order_by("-id")[:7],
        'latestpost': latestpost,
        'bisness': bisness,
    }
    return render(request, 'index.html', context)
