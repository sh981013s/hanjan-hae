from django.shortcuts import render

app_name = 'main'

def index(request):
    return render(request, "./base/index.html")

def tmp(request):
    return render(request, "./community/write.html")

def past(request):
    return render(request, "./community/list.html")


