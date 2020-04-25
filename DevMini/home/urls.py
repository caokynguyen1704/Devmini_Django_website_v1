from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('', views.index,name='home'),
   path('profile/',views.profile,name="profile"),
   path('code/',views.code,name="code"),
   path('register/', views.register, name="register"),
   path('edit/', views.edit, name="edit"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]