from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', communityMain, name="communityMain"),
    path('<int:post_id>', communityDetail, name="communityDetail"),
    path('<int:post_id>/comment', create_comment, name="comment"),
]