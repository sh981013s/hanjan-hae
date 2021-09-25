from django.shortcuts import render, redirect
from .models import Todaylog
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# 오늘의기록 메인
@login_required
def todaylogMain(request):
    if request.method == "GET":

        posts = Todaylog.objects.all()
        return render(request, 'community/list.html', {'posts':posts})
    else :
        posts = Todaylog.objects.all()
        return render(request, 'community/list.html', {'posts':posts})




def todaylogWrite(request):
    if request.method == 'POST':
        post = Todaylog()
        post.category = request.POST['category']
        post.drink = request.POST['drink']
        post.rating_content = request.POST['rating_content']
        post.author = request.user
        post.save()
        return render(request, 'community/write.html')
    else:
        return render(request, 'community/write.html')

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
