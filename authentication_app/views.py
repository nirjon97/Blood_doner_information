from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm
from .models import UserProfile

# Create your views here.
#login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, 'Your username or password is invalid.')

    context={

    }

    return render(request,'page 2 (login form).html',context)

#register view
def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()

            return redirect('Home')
        else:
            messages.warning(request, "Your new and reset password is not matching")
            print("Your new and reset password is not matching")
    else:
        form = SignUpForm()

    context={
       'form': form

    }

    return render(request,'page 3 (register).html',context)




#logout view
def user_logout(request):
    logout(request)
    return redirect('login_register_option')