from django.urls import path
from . import views

urlpatterns = [


    path('register/',views.UserRegister,name="UserRegister"),
    path('Login/',views.UserLogin,name="Login"),
    path('Logout/',views.UserLogout,name="Logout"),
    path('confirmlogout/',views.ConfirmLogout,name="ConfirmLogout"),


]