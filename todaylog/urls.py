from django.urls import path
from .views import *

app_name = 'todaylog'

urlpatterns = [
    path('todaylog', todaylogMain, name="todaylogMain"),
    path('todaylog/write', todaylogWrite, name="todaylogWrite"),
    path('todaylog/edit', todaylogEdit, name="todaylogEdit"),
    path('todaylog/delete', todaylogDelete, name="todaylogDelete"),
]