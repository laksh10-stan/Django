from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):        #atleast one arg
    return HttpResponse("Hello World!") #each view must have one HttpResponse
    
