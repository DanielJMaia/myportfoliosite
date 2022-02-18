from django.shortcuts import render, redirect, reverse
from websites.models import Website
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                          email,
                          message,
                          from_email,
                          ['djohnsonmaia@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    
    template = 'home/index.html'
    websites = Website.objects.all()
    context = {
        'websites': websites,
        'form': form,
    }

    return render(request, template, context)


def successView(request):
    messages.success(request, "Message successfully sent!")
    return redirect(reverse('home'))