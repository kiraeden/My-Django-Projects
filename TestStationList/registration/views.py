from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

class RegistrationView(generic.FormView):
    template_name = 'registration/login.html'
    model = User

def register(request):
    if request.POST['username'] != "":
        if request.POST['password'] == request.POST['confirm']:
            newUser = User.create(username=request.POST['username'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'])
            newUser.save()
        else:
            pass
    else:
        pass