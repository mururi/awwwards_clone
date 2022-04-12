from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import RegisterForm, ProjectForm
from django.contrib.auth.decorators import login_required


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

@login_required(login_url = '/register')
def submit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = current_user
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    return render(request, 'submit.html', {"form": form})