from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from .models import code,script

urlpatterns = [
   path('', views.index,name='home'),
   path('profile/',views.profile,name="profile"),
   path('code/',views.codeinhere,name="code"),
   path('vietbai/',views.codex,name="vietbai"),
   
   path('vietbaihoc/',views.script,name="vietbaihoc"),
   path('post/',views.list,name="baidang"),
   
   path('hocscript/',views.script_list,name="baihoc"),
    path('rank/',views.rank,name="rank"),
   path('register/', views.register, name="register"),
   path('thongbao/', views.thongbao, name="thongbao"),
   path('edit/', views.edit, name="edit"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('infor/<int:id>/', views.inforRank),
   path('post/<int:pk>/', views.post1, name='post'),
   path('adminsite/', views.adminsite, name="admin"),
   path('like/<int:id>',views.like,name="like"),

 
]



