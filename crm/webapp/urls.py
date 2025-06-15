from django.urls import path
from . import views

urlpatterns = [
    
path('', views.home, name =""),
path('register', views.register, name="register"),
path('my-login', views.login, name="my-login"),
path('dashboard', views.dashboard, name="dashboard"),
path('user-logout', views.user_logout, name="user-logout"),

]
