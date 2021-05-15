from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome our hairpiece corner.. We have the best hairs</h1>')

def new(request):
    return HttpResponse("<h1>We just stocked up on new products. Feel free to look around</h1>")