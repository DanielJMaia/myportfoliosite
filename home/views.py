from django.shortcuts import render
from websites.models import Website

def index(request):
    template = 'home/index.html'
    websites = Website.objects.all()
    context = {
        'websites': websites,
    }
    return render(request, template, context)
