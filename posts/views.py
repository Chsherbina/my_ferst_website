"""
Model.objects.all() = возвращает все записи из базы даных
Model.objects.get() = возвращает одну запись из базы даных
Model.objects.filter() = возвращает записи из базы даных по условиям
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse

from posts.models import Post


def welcome(request):
    if request.method == 'GET':
        return HttpResponse("Welcome to my website")


def main_page(request):
    return render(request, 'main_page.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_create.html')
    elif request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        rate = request.POST.get('rate')
        Post.objects.create(image=image, title=title, content=content, rate=rate)
        return redirect('/posts/')
