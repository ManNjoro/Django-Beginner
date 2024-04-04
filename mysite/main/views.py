from django.shortcuts import render
from django.http import HttpResponse
from .models  import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    ls = ToDoList.objects.all()
    print("ls: ",ls)
    return render(response, "main/home.html", {"ls": ls})

def create(response):
    return render(response, "main/create.html", {})