"""
URL configuration for blog2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import welcome, main_page, post_list_view, post_detail_view, post_create_view
from user.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('', main_page),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('posts/create/', post_create_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', profile_view, name='profile'),
    path('post/<int:post_id>/update', post_detail_view, name='post-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)