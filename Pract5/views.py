# Create your views here.
from django.http import HttpResponse

def home (request):
	return HttpResponse("This is home!")

def help (request):
        return HttpResponse("This is help!")

def about (request):
        return HttpResponse("This is about!")

