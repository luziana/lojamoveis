from django.shortcuts import render


def index(request):
    return render(request, "home.html")


def cadastros(request):
    return render(request, "cadastros.html")