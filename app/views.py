from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    de=datetime.datetime.now()
    d={'data':'Data Is PResented','c':1,'de':de}
    return render(request,'built_in_filters.html',d)