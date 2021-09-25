from django.shortcuts import render

app_name = 'main'

def index(request):
    return render(request, "./base/index.html")



