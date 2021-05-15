from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome. Our beddings are of the best quality and would suite your rooms</h1>')

def new(request):
    return HttpResponse("<h1>Here are our new products, Please feel free to look around</h1>")