from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def nextpage(request):
    return render(request,'index2.html')

