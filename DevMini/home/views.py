from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')

from .forms import RegistrationForm, EditProfile, EditCode
from django.http import HttpResponseRedirect 
def profile(request):
   return render(request, 'pages/profile.html')

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
      form=EditCode(request.POST)
      if form.is_valid():
         form.savecode(nick)
         return HttpResponseRedirect('/')
   return render(request, 'pages/code.html', {'form': form})

from .models import code
def list(request):
   Data = {'Code': code.objects.all().order_by('-Date')}
   return render(request, 'pages/baidang.html', Data)
