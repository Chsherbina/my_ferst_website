from django.contrib import admin
from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date', 'category', 'rate')
    list_editable = ('rate',)
    list_display_links = ('title', 'created_date', 'updated_date', 'category')
    list_filter = ('category', 'created_date', 'updated_date')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
