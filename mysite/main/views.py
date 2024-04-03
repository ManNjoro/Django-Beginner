from django.shortcuts import render
from django.http import HttpResponse
from .models  import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse(f"<h1>{ls.name}</h1>")