from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Skills
from django.contrib.auth.decorators import login_required
import random


# Create your views here.
@login_required
def show_skills(request):
    user_obj = User.objects.all()
    return render(request=request, template_name='skills/users_dashboard.html', context={'users': user_obj})


@login_required
def users_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        skills = request.POST.get('skills')
        percentage = request.POST.get('percentage')
        email = request.POST.get('email')
        print(first_name, last_name, username, skills, percentage, email)

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken!')
            return redirect('skills')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already taken!')
            return redirect('skills')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
            Skills.objects.create(skills=skills, percentage=percentage, user_obj=user)
            user.save()
            print('User Created!')
            return redirect('skills')

    else:
        return render(request, 'skills/users_dashboard.html')


@login_required
def users_edit(request):
    if request.method == 'POST':
        rec_id = request.POST.get('edit_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        skills = request.POST.get('skills')
        percentage = request.POST.get('percentage')
        email = request.POST.get('email')

        if True:
            User.objects.filter(id=rec_id).update(first_name=first_name, last_name=last_name, email=email,
                                                  username=username)
            user = User.objects.filter(id=rec_id).first()
            if not Skills.objects.filter(user_obj_id=user):
                Skills.objects.create(skills=skills, percentage=percentage, user_obj=user)
            Skills.objects.filter(user_obj_id=rec_id).update(skills=skills, percentage=percentage)

            return redirect('skills')

    else:
        return render(request, 'skills/users_dashboard.html')


@login_required
def users_delete(request):
    if request.method == "POST":
        user = User.objects.filter(id=request.POST.get('rec_id'))
        user.delete()
        return redirect('skills')
    return render(request, 'skills/users_dashboard.html')


@login_required
def chart_view(request):
    """
       pieChart page
       """
    labels = []
    data = []
    color = []

    queryset = User.objects.all()

    for user in queryset:
        try:
            if user.user_obj.percentage:
                labels.append(user.username)
                data.append(user.user_obj.percentage)
        except Exception as e:
            print(e)

    for itm in range(0, len(labels)):
        r = lambda: random.randint(0, 255)
        color.append('#%02X%02X%02X' % (r(), r(), r()))
    data = {'labels': labels, 'data': data, 'color': color}
    return render(request, 'users/pie_chart.html', context=data)
