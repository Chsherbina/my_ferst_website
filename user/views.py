from django.shortcuts import render
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')

