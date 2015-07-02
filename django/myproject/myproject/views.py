# cat views.py
import datetime
from django.http import HttpResponse
def hello(request):
	return HttpResponse("Hello world!!!")

def index(request):
	return HttpResponse("Home page")

def currenttime(request):
	d = datetime.datetime.now()
	return HttpResponse("Current Time : {0}".format(d))


