from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import RegisterForm


def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects": projects})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})