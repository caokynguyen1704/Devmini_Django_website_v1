from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    Point=models.IntegerField(default=0)
    Linhvuc=models.CharField(max_length=500,default="Không có")
    Namsinh=models.IntegerField(default=0)
    Chucvu=models.CharField(max_length=500,default="Không có")
    Noio=models.CharField(max_length=500,default="")
    Uid=models.IntegerField(default=0)
class ThongBao(models.Model):
    Thongbao=models.TextField(default="Không có thông báo")

class code(models.Model):
    Loai=models.CharField(max_length=200,default="Chưa có")
    Title=models.CharField(max_length=200,default="")
    Code=models.TextField()
    Date=models.DateTimeField(auto_now=True)
    User=models.CharField(max_length=200,default="")
    Like=models.IntegerField(default=1)
    Unlike=models.IntegerField(default=1)
    HuongUng=models.IntegerField(default=0)
    Img=models.ImageField(null=True)

class script(models.Model):
    Tieude=models.CharField(max_length=200, default="")
    Noidung1=models.TextField(default="")
    Code1=models.TextField(default="")
    Noidung2=models.TextField(default="")
    Code2=models.TextField(default="")
    Noidung3=models.TextField(default="")
    Code3=models.TextField(default="")
    Date=models.DateTimeField(auto_now=True)
    User=models.CharField(max_length=300,default="")

from django.conf import settings

class Comment(models.Model):
    post = models.ForeignKey(code, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField(default=0)
