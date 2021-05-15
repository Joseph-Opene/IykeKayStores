from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse('''
    <h1>WELCOME TO IYKEKAYSTORES</h1>
    <h1>PLEASE LOOK AROUND FOR ALL OUR PRODUCTS AND WE SELL AT THE BEST PRICE</h1>
    <h1>FEEL FREE TO CHECK OUT OUR BLOG CORNER AND KEEP YOURSELF UPDATED WITH THE LATEST NEWS AND TRENDS</h1>
    <h1>THANKS FOR VISITING US AND WE HOPE TO SEE YOU AGAIN</h1>
    ''')