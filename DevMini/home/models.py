from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
class hocvien(models.Model):
    hovaten=models.CharField(max_length=200,default="No name")
    namsinh=models.IntegerField(default=2010)
    chuyencan=models.IntegerField(default=0)
    diem_baihoc=models.IntegerField(default=0)
    diem_kiemtratuan=models.IntegerField(default=0)
    diem_kiemtrathang=models.IntegerField(default=0)
    diem_ketthuc=models.IntegerField(default=0)
    tongdiem=models.IntegerField(default=0)
    chuthich=models.CharField(max_length=999999,default="Chưa có điểm mới")
    objects = models.Manager() 
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
    objects = models.Manager() 
class MyUser(AbstractUser):
    Point=models.IntegerField(default=0)
    Linhvuc=models.CharField(max_length=500,default="Không có")
    Namsinh=models.IntegerField(default=0)
    Chucvu=models.CharField(max_length=500,default="Không có")
    Noio=models.CharField(max_length=500,default="")
    Uid=models.IntegerField(default=0)
class ThongBao(models.Model):
    Thongbao=models.TextField(default="Không có thông báo")
class Comment(models.Model):
    post = models.ForeignKey(code, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField(default=0)
class sharecode(models.Model):
    Title=models.CharField(max_length=200,default="Chưa có tiêu đề")
    Gioithieu=models.TextField()
    Link=models.CharField(max_length=500,default="")
    Chucnang=models.TextField()
    Date=models.DateTimeField(auto_now=True)
    User=models.CharField(max_length=200,default="")
class Comment_share(models.Model):
    post = models.ForeignKey(sharecode, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField(default=0)
