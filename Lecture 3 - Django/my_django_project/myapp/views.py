from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")

def marilyn(request):
    return HttpResponse("Hello, Marilyn!")

def webgemini(request):
    return HttpResponse("Hello, WebGemini! The best website builder in RSA")

def greet(request, name):
    return render(request, "myapp/greet.html", {
        "name": name.capitalize()
    })