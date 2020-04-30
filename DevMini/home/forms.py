from django import forms
import re
#from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from home.models import MyUser,code, script
class EditCode(forms.Form):
    loai=forms.CharField(max_length=1000)
    codeedit=forms.CharField(widget=forms.Textarea)
    title=forms.CharField(max_length=200)
    img=forms.ImageField()
    def savecode_hasImg(self,nick):
        codea=code()
        codea.Loai=self.cleaned_data['loai']
        codea.Code=self.cleaned_data['codeedit']
        codea.Title=self.cleaned_data['title']
        codea.Img=self.cleaned_data['img']
        codea.User=nick
        codea.save()
    def savecode_noImg(self,nick):
        codea=code()
        codea.Loai=self.cleaned_data['loai']
        codea.Code=self.cleaned_data['codeedit']
        codea.Title=self.cleaned_data['title']
        codea.User=nick
        codea.save()
class LikeUnlike(forms.Form):
    likeunlike=forms.IntegerField()
    def tangLike(self,id,nick):
        post = code.objects.get(id=id)
        username=MyUser.objects.get(username=nick)
        if self.cleaned_data['likeunlike']==1:
            post.Like=post.Like + 1 
            post.HuongUng=post.Like/post.Unlike
            post.save()
        elif self.cleaned_data['likeunlike']==2:
            post.Unlike=post.Unlike + 1
            post.HuongUng=post.Like/post.Unlike
            post.save()
        elif self.cleaned_data['likeunlike']==3 and (post.User==nick or username.is_superuser):
            post.delete()

class AdminSite(forms.Form):
    id=forms.IntegerField()
    chucvu=forms.CharField(max_length=200)
    linhvuc=forms.CharField(max_length=200)
    def edit_infor(self):
        username=MyUser.objects.get(id=self.cleaned_data['id'])
        username.Chucvu=self.cleaned_data['chucvu']
        username.Linhvuc=self.cleaned_data['linhvuc']
        username.save()
class EditProfile(forms.Form):
    firstname=forms.CharField(label="Họ",max_length=100)
    lastname=forms.CharField(label="Tên",max_length=100)
    namsinh=forms.IntegerField(label="Năm sinh")
    uid=forms.IntegerField(label="uid")
    noio=forms.CharField(label="Nơi ở",max_length=200)
    def edit_OK(self,nick):
        username=MyUser.objects.get(username=nick)
        username.first_name=self.cleaned_data['firstname']
        username.Noio=self.cleaned_data['noio']
        username.last_name=self.cleaned_data['lastname']
        username.Namsinh=self.cleaned_data['namsinh']
        username.Uid=self.cleaned_data['uid']
        username.save()

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại pass', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        MyUser.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self,id_user, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.id_user=id_user
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]

class EditScript(forms.Form):
    code1=forms.CharField(widget=forms.Textarea)
    code2=forms.CharField(widget=forms.Textarea)
    code3=forms.CharField(widget=forms.Textarea)
    noidung1=forms.CharField(widget=forms.Textarea)
    noidung1=forms.CharField(widget=forms.Textarea)
    noidung1=forms.CharField(widget=forms.Textarea)
    title=forms.CharField(max_length=200)
    def savecode_hasImg(self,nick):
        codea=script()
        codea.Code1=self.cleaned_data['code1']
        codea.Code2=self.cleaned_data['code2']
        codea.Code3=self.cleaned_data['code3']
        codea.Noidung1=self.cleaned_data['noidung1']
        codea.Noidung2=self.cleaned_data['noidung2']
        codea.Noidung3=self.cleaned_data['noidung3']
        codea.Tieude=self.cleaned_data['title']
        codea.User=nick
        codea.save()

        