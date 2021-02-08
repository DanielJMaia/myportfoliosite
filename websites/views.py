from django.shortcuts import render


def websites(request):
    template = 'websites/websites.html'
    return render(request, template)

