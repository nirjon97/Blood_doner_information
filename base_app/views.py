from django.shortcuts import render

# Create your views here.

def login_register_option(request):

    context={

    }

    return render(request,'page 1 (login and register button).html',context)
