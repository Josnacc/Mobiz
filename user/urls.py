from django.urls import path
from . import views

   
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('student', views.student, name='student'),
    path('staff', views.staff, name='staff'),
    path('admin', views.admin, name='admin'),
    path('editor', views.editor, name='editor'),
    
    path('logout', views.logout, name='logout'),



    
]
