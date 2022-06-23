from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from mainapp.models import Item
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        user=User.objects.create(username=request.POST['kid-name'])
        login(request,user)
        return redirect('/')
    return render(request,'register.html')

def library(request):
    if request.user.is_anonymous or not request.user.is_authenticated:
        return redirect('/register')

    stories=Item.objects.filter(type='1')
    movies=Item.objects.filter(type='2')
    songs=Item.objects.filter(type='3')
    return render(request,'library.html',{
        'stories':stories,
        'movies':movies,
        'songs':songs
    })


def addItem(request):
    if request.method=='POST':
        item=Item.objects.create(name=request.POST['title'],type=request.POST['type'],url=request.POST['link'],image=request.FILES['img'])
        return redirect('/library')
    return render(request,'addItem.html')
def updateItem(request,pk):
    item=Item.objects.get(pk=pk)
    if request.method=='POST':
        item.name=request.POST['title']
        item.url=request.POST['link']
        if 'img' in request.FILES:  
            item.image=request.FILES['img']
        item.save()

        return redirect('/library')
    return render(request,'update.html',{"item":item})
def deleteItem(request,pk):
    item=Item.objects.get(pk=pk)
    item.delete()
    return redirect('/library')

def addItem(request):
    if request.method=='POST':
        item=Item.objects.create(name=request.POST['title'],type=request.POST['type'],url=request.POST['link'],image=request.FILES['img'])
        return redirect('/library')
    return render(request,'addItem.html')
def loginV(request):
    if request.method=='POST':
        if not request.user.is_anonymous and request.user.is_authenticated:
            logout(request)
        user=authenticate(request,username=request.POST['username'],password=request.POST['pass'])
        if user:
            if user.is_superuser:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,'لست مشرف')
        else:
            messages.error(request,'خطأ بالمعلومات')
    return render(request,'login.html')

