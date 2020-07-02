from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .models import code,sharecode

urlpatterns = [
   path('', views.index,name='home'),
   path('profile/',views.profile,name="profile"),
   path('code/',views.code_list,name="code"),
   path('vietbai/',views.codex,name="vietbai"),
   path('sharecode/',views.share,name="share"),
   path('post/',views.list,name="baidang"),
   path('rank/',views.rank,name="rank"),
   path('register/', views.register, name="register"),
   path('thongbao/', views.thongbao, name="thongbao"),
   path('edit/', views.edit, name="edit"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('infor/<int:id>/', views.inforRank),
   path('code/<int:pk>/', views.post2,name='codex'),
   path('post/<int:pk>/', views.post, name='post'),
   path('adminsite/', views.adminsite, name="admin"),
   path('like/<int:id>',views.like,name="like"),
   path('learn/',views.hocscript,name="learn"),
   path('hocvien/',views.hocvien,name="hocvien"),
]



