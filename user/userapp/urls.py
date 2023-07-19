from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.home,name='home'),
    path('',views.UserRegister,name="UserRegister"),
    path('Login/',views.UserLogin,name="Login"),
    path('Logout/',views.UserLogout,name="Logout"),
    path('confirmlogout/',views.ConfirmLogout,name="ConfirmLogout"),


]