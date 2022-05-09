from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post

# Create your views here.

def main(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'main.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'detail.html', context)

def write(request):
    if request.method == 'POST':
        post = Post(title=request.POST.get('title'), content=request.POST.get('content'), date=timezone.now())
        post.save()
        return redirect('/board/main/')
    else: # request.method == 'GET':
        return render(request, 'write.html')