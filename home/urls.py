from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('login',views.logine,name='login'),
    path('user', views.user, name='user'),
    path('register',views.register,name='register')
]