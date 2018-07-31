from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def users(request):
	user_list = User.objects.all()
	context = {
		"users" : user_list
	}
	return render(request, 'apptwo/index.html', context)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'apptwo/help.html', context=helpdict)
