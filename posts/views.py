"""
Model.objects.all() = возвращает все записи из базы даных
Model.objects.get() = возвращает одну запись из базы даных
Model.objects.filter() = возвращает записи из базы даных по условиям
"""


from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post


def welcome(request):
    return HttpResponse("Welcome to my website")


def main_page(request):
    return render(request, 'main_page.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})