from django.shortcuts import render
import psycopg2
from main.models import  ProductInfo

# Create your views here.
def index(request, pk):
    owner_obj = ProductInfo.objects.get(pk=pk)

    context = {
        "drivers": owner_obj,

    }
    return render(request, "index.html", context)