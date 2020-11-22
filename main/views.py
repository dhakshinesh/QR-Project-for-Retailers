from django.shortcuts import render
import psycopg2

# Create your views here.
def index(request):
    return "Hello"