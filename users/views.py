from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth


def registration_request(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        is_super_user = request.POST.get('is_super_user')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name,
                                                is_superuser=True if is_super_user == 'on' else False)
                user.save()
                print('User Created!')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('register')
    else:
        return render(request, 'users/registration.html')


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('skills')
        else:
            messages.info(request, 'User not yet registered')
            return redirect('login')

    return render(request=request, template_name="users/login.html")


def logout_request(request):
    logout(request)
    return render(request=request, template_name="users/login.html")


def admin_request(request):
    return render(request=request, template_name="users/admin_dash.html")


def employee_request(request):
    return render(request=request, template_name="users/pie_chart.html")
