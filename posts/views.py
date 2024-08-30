"""
Model.objects.all() = возвращает все записи из базы даных
Model.objects.get() = возвращает одну запись из базы даных
Model.objects.filter() = возвращает записи из базы даных по условиям
"""

"""posts = [ post1, post2, post3, post4, post5, post6, post7, post8, post9, post10, post11, post12, post13, post14, post15]
limit = 3, page = 1
formula
start = page-1 * limit
(3-1)*3=6
end = 1*3 = 3
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from posts.forms import SearchForm, PostUpdateForm
from posts.models import Post, CommentForm


def welcome(request):
    if request.method == 'GET':
        return HttpResponse("Welcome to my website")


def main_page(request):
    return render(request, 'main_page.html')


@login_required(login_url='/login/')
def post_list_view(request, orderings=None):
    search = request.GET.get('search')
    tags = request.GET.getlist('tags')
    ordering = request.GET.get('ordering')
    searchform = SearchForm(request.GET)
    page = int(request.GET.get('page', 1))
    posts = Post.objects.all()
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    if tags:
        posts = posts.filter(tags__id__in=tags)
    if orderings:
        posts = posts.order_by(orderings)

    limit = 3
    max_pages = posts.count() / limit
    if round(max_pages) < max_pages:
        max_pages = round(max_pages) + 1
    else:
        max_pages = round(max_pages)

    start = (page-1) * limit
    end = page * limit
    posts = posts[start:end]
    context = {'posts': posts, 'search_form': searchform, 'max_pages': range(1, max_pages + 1)}
    return render(request, 'posts/post_list.html', context = context)


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'comment_form': comment_form})


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

@login_required(login_url="login")
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostUpdateForm(instance=post)
        return render(request, "posts/post_update.html", {"form": form})
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILTER, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', {'form': form})
        form.save()
        return redirect('/profile/')


