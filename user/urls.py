from django.urls import path
from . import views
from calc_alc import views as cV



app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('mypage/',views.mypage, name='mypage'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('farewell/', views.userDelete, name="delete_success"),
    path('signout/', views.signout, name='signout'),
    path('alcohol/', cV.home, name='alcohol'),

]
