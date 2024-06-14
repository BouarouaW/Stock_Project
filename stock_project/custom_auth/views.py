from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .form import LoginForm, RegistrationForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'custom_auth/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(email=email)
                if user.check_password(password):
                    print(user.is_staff)
                    if user.is_staff:
                        return render(request, 'admin_panel/dashboard.html', {'admin_name': user.get_username()})
                    else:
                        return render(request, 'employe_panel/dashboard.html', {'employe_name': user.get_username()})
                else:
                    error_message = "Invalid email or password."
            except CustomUser.DoesNotExist:
                error_message = "Invalid email or password."
    else:
        form = LoginForm()
    return render(request, 'custom_auth/login.html', {'form': form})
