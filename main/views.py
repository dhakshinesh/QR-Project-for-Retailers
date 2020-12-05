from django.shortcuts import render
import psycopg2
from main.models import  ProductInfo

# Create your views here.
def index(request):
    owner_obj = ProductInfo.objects.all()

    context = {
        "data": owner_obj,
    }
    return render(request, "index.html", context)

def generate(request):
    return render(request, "generate.html")

def Login(request):
    return render (request, "login.html")
def signup(request):
    return render (request, "signup.html")