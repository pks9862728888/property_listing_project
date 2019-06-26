from django.shortcuts import render, redirect
from django.views.generic import (TemplateView)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from contacts.models import Contacts

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Invalid Username or Password.")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


@login_required(redirect_field_name='accounts:login')
def logoutView(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out :)")
        return redirect("pages:index")
    else:
        return redirect('pages:index')

def registerView(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password1 == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken.")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already registered.")
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name,
                                                    last_name=last_name, email=email,
                                                    password=password1)
                    user.save();
                    messages.success(request, 'You are successfully registered & can login :)')
                    return redirect('accounts:login')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('accounts:register')
    else:
        return render(request, "accounts/register.html")


@login_required(redirect_field_name='accounts:login')
def dashboardView(request):
    user_contacts = Contacts.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contacts
    }
    return render(request, "accounts/dashboard.html", context)

