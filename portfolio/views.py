from django.shortcuts import render
from .models import Project
from blog import views
# Create your views here.

def home(request):
    project = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': project})

