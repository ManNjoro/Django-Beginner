from django.shortcuts import render
from django.http import HttpResponse
from .models  import ToDoList, Item
from .forms import CreateNewList

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
    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})