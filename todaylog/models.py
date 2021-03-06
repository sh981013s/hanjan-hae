from django.db import models
from django.contrib.auth import get_user_model

class Todaylog(models.Model):
    drink = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
		('soju', '소주'),
        ('beer', '맥주'),
        ('makgeolli', '막걸리'),
        ('liquor', '양주'),
        ('wine', '와인'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='soju')
    rating_content = models.TextField(max_length=100)
    
class Comment(models.Model):
    post_id = models.ForeignKey(Todaylog, on_delete=models.CASCADE, db_column="post_id")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)