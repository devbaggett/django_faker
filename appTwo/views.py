from django.shortcuts import render
# from .models import *
from .forms import NewUserForm


def index(request):
    return render(request, 'apptwo/index.html')


def users(request):
    # create object and assign it to instance of NewUserForm
    form = NewUserForm()

    # if submit request.method is POST, we pass in request.POST
    if request.method == "POST":
        form = NewUserForm(request.POST)

        # check if valid or not
        if form.is_valid():
            # save and commit to DB
            form.save(commit=True)
            # go back to homepage
            return index(request)
        else:
        	print('ERROR: FORM INVALID')

    # pass in form object to users.html
    return render(request, 'apptwo/users.html', {'form': form})


def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'apptwo/help.html', context=helpdict)
