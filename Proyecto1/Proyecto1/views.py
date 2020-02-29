from django.shortcuts import render
from .forms import Signupform, Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def pagelogin(request):
  
    uservalue=''
    passwordvalue=''

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'siteusers/login.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'siteusers/login.html', context )

    else:
        context= {'form': form}
        return render(request, 'siteusers/login.html', context)
