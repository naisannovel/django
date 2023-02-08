from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(req):
    print("req", req)
    return JsonResponse({"name":"naisan novel"})
