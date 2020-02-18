from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):        #atleast one arg
    # return HttpResponse("Hello World!") #each view must have one HttpResponse
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_me':'Now I am coming from fistapp/index.html'}
    return render(request, 'first_app/index.html', context=date_dict)
