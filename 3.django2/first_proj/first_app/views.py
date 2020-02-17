from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):        #atleast one arg
    # return HttpResponse("Hello World!") #each view must have one HttpResponse
    my_dict = {'insert_me':'Now I am coming from fistapp/index.html'}
    return render(request, 'first_app/index.html', context=my_dict)
