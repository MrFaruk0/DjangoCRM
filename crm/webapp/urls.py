from django.urls import path
from . import views

urlpatterns = [
    
path('', views.home, name =""),

path('register', views.register, name="register"),

path('my-login', views.login, name="my-login"),

path('user-logout', views.user_logout, name="user-logout"),

#CRUD

path('dashboard', views.dashboard, name="dashboard"),

path('create', views.create_client, name="create"),

path('update/<int:pk>', views.update_client, name="update"),

path('view/<int:pk>', views.view_client, name="view"),

path('delete/<int:pk>', views.delete_client, name="delete"),


]
