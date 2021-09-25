from django.shortcuts import render, redirect
from .models import Todaylog
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# 오늘의기록 메인
@login_required
def todaylogMain(request):
    posts = Todaylog.objects.all().filter(author=request.user)
    return render(request, 'todaylog/todaylogMain.html', {'posts':posts})

def todaylogWrite(request):
    if request.method == 'POST':
        post = Todaylog()
        post.drink = request.POST['drink']
        post.category = request.POST['category']
        post.pub_date = timezone()
        post.author = request.user
        post.rating = request.POST['rating']
        post.rating_content = request.POST['rating_content']
        post.public = request.POST['public']
        post.image = request.FILES['image']
        post.save()
    else:
        return render(request, 'todaylog/todaylogWrite.html')

def todaylogEdit(request, id):
    if request.method == 'POST':
        post = Todaylog.objects.get(id=id)
        post.drink = request.POST['drink']
        post.category = request.POST['category']
        post.pub_date = timezone()
        post.author = request.user
        post.rating = request.POST['rating']
        post.rating_content = request.POST['rating_content']
        post.public = request.POST['public']
        post.image = request.FILES['image']
        post.save()
    else:
        post = Todaylog.objects.get(id=id)
        return render(request, 'todaylog/todaylogEdit.html', 'post:post')

def todaylogDelete(request, id):
    post = Todaylog.objects.get(id=id)
    post.delete()
    return redirect('todaylog:main')
