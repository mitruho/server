from django.shortcuts import render
from .models import Interest,Project
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'core/index.html')
def about_me(request):
    interests = Interest.objects.all()
    context = {'interests':interests}
    return render(request, 'core/about_me.html',context=context)
def project(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'core/project.html',context=context)
def ya_rabotayu_s(request):
    return render(request, 'core/ya_rabotayu_s.html')