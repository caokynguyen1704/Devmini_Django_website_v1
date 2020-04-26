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

class code(models.Model):
    Title=models.CharField(max_length=200,default="")
    Code=models.TextField()
    Date=models.DateTimeField(auto_now=True)
    User=models.CharField(max_length=200,default="")
    Like=models.IntegerField(default=0)
    Unlike=models.IntegerField(default=0)
    Img=models.ImageField(null=True)