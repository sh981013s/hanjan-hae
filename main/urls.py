from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('tmp', views.tmp, name='tmp'),
    path('past', views.past, name='past'),
]