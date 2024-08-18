from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
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
