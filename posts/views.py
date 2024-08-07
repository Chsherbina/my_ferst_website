from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to my website")


def main_page(request):
    return render(request, 'main_page.html')
