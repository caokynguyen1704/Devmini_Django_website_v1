from django.contrib import admin
from .models import MyUser, code, ThongBao, script
# Register your models here.
admin.site.register(MyUser)
admin.site.register(script)
#admin.site.register(code)
from django.contrib import admin

# Register your models here.
from .models import code, Comment
admin.site.register(ThongBao)
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Date']
    list_filter = ['Date']
    search_fields = ['Title']
    inlines = [CommentInline]
 
admin.site.register(code,PostAdmin)