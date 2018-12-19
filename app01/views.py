from django.shortcuts import render
from app01.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')