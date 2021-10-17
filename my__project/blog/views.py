from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    response = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood')
    resp = response.json()
    meals = resp['meals']
    return render(request, 'blog/index.html',{'meals': meals})

def specific(request):
    return HttpResponse("specific page")

# def article(request,article_id):
#     # return HttpResponse("im "+str(article_id)+" years old")
#     return render(request,'blog/index.html',{'article':article_id})


