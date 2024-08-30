from django.contrib.auth.models import User
from django.db import models

from posts import forms


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True, verbose_name='Текст поста')
    rate = models.IntegerField(default=0, verbose_name='Оценка')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    text = models.TextField()
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']