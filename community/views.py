from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from todaylog.models import Todaylog, Comment
from django.contrib.auth.decorators import login_required

def communityMain(request):
    community_list = Todaylog.objects.all() 
    paginator = Paginator(community_list, 4)
    page = request.GET.get('page') 
    posts = paginator.get_page(page) 
    return render(request, 'community/community_main.html', {'posts':posts})

def communityDetail(request, post_id): 
    post = get_object_or_404(Todaylog, pk = post_id) 
    comments = Comment.objects.filter(post_id=post_id, comment_id__isnull=True)
    return render(request, 'community/community_detail.html', {'post':post, 'comments':comments})

@login_required
def create_comment(request, post_id):
    if request.method == 'POST':
        comment = Comment()
        comment.post_id = Todaylog.objects.get(pk=post_id)
        comment.author = request.user
        comment.save()
    return redirect('/community/' + str(post_id))
