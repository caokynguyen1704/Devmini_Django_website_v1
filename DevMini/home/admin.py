from django.contrib import admin
from .models import MyUser, code, ThongBao, sharecode
# Register your models here.
admin.site.register(MyUser)

#admin.site.register(code)
from django.contrib import admin

# Register your models here.
from .models import code, Comment, Comment_share
admin.site.register(ThongBao)
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Date']
    list_filter = ['Date']
    search_fields = ['Title']
    inlines = [CommentInline]
class CommentInline_share(admin.TabularInline):
    model = Comment_share

class PostAdmin_share(admin.ModelAdmin):
    list_display = ['Title', 'Date']
    list_filter = ['Date']
    search_fields = ['Title']
    inlines = [CommentInline_share]
 
admin.site.register(code,PostAdmin)
admin.site.register(sharecode,PostAdmin_share)