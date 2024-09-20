from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    # path('reportForm/',reportForm , name='reportForm'),
    path('userForm/',userForm , name='userForm'),   
    path('userTable/',userTable , name='userTable'),   
    path('soft_delete_user/<int:user_id>/', soft_delete_user, name='soft_delete_user'),
    path('',loginForm , name='loginForm'),   
    path('logout_view/',logout_view , name='logout_view'), 
    path('loginForm/',loginForm , name='loginForm'), 
    path('indexForm/', indexForm, name='indexForm'),

]