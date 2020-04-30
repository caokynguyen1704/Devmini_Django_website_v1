import requests
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from home.models import code, Comment,ThongBao,script
from .forms import CommentForm,EditScript
from django.http import HttpResponseRedirect
# Create your views here.
from django.db import models

def index(request):
    Data = {'ad': ThongBao.objects.all()}
    return render(request, 'pages/home.html',Data)
def vietbai(request):
   return render(request, 'pages/code.html')
def codeinhere(request):
   return render(request, 'pages/code_main.html')
from .forms import RegistrationForm, EditProfile, EditCode, LikeUnlike, AdminSite
from django.http import HttpResponseRedirect 
def profile(request):
   return render(request, 'pages/profile.html')

def adminsite(request):
   form=AdminSite()
   if request.method=='POST':
      form=AdminSite(request.POST)
      if form.is_valid():
         form.edit_infor()
         return HttpResponseRedirect('/')
   return render(request,'pages/admin.html', {'form':form})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

from home.models import MyUser
def edit(request):
   form = EditProfile()
   nick=request.user.username
   if request.method == 'POST':
      form=EditProfile(request.POST)
      if form.is_valid():
         form.edit_OK(nick)
         return HttpResponseRedirect('/')
   return render(request, 'pages/profile-edit.html', {'form': form})

def codex(request):
   form = EditCode()
   nick=request.user.username
   if request.method == 'POST':
      form=EditCode(request.POST,request.FILES)
      if form.is_valid():
         upload(request.FILES['img'])
         form.savecode_hasImg(nick)
      else:
         form.savecode_noImg(nick)
      return HttpResponseRedirect('/')
   return render(request, 'pages/code.html', {'form': form})

def script(request):
   form = EditScript()
   nick=request.user.username
   if request.method == 'POST':
      form=EditScript(request.POST,request.FILES)
      if form.is_valid():
         form.savecode_hasImg(nick)
      return HttpResponseRedirect('/')
   return render(request, 'pages/vietscript.html', {'form': form})


def list(request):
   Data = {'Code': code.objects.all().order_by('-Date')}
   return render(request, 'pages/baidang.html', Data)


def upload(f): 
    file = open(f.name, 'wb+') 
    for chunk in f.chunks():
        file.write(chunk)


def script_list(request):
   Data = {'script': script.objects.all().order_by('-Date')}
   return render(request, 'pages/hocscript.html', Data)

def rank(request):
   Data = {'Rank': MyUser.objects.all().order_by('-Point')}
   return render(request, 'pages/rank.html', Data)

def inforRank(request,id):
   rank = MyUser.objects.get(id=id)
   return render(request,'pages/infor.html',{'rank':rank})


# Create your views here.

def post1(request, pk):
    post = code.objects.get(id=pk)
    form = CommentForm()
    if request.method == "POST":
        id_user=request.user.id
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save(id_user)
            return HttpResponseRedirect(request.path)
    return render(request, "pages/post.html", {"post": post, "form": form})

def like(request, id):
   nick=request.user.username
   post = code.objects.get(id=id)
   form=LikeUnlike()
   if request.method=='POST':
      form=LikeUnlike(request.POST)
      if form.is_valid():
         form.tangLike(id,nick)
         return HttpResponseRedirect("/")
   return render(request, 'pages/like.html', {'post': post,"form":form})

def thongbao(request):
   form=ThongBaoAdmin()
   if request.method=='POST':
      form=ThongBaoAdmin(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
   return render(request, 'pages/thongbao.html', {"form":form})
