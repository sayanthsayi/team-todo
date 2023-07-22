from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<str:pk>/',views.update_task,name='update'),
]
