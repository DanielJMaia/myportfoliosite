from django.contrib import admin
from .models import Website

class WebsiteAdmin(admin.ModelAdmin):

    fields = ['name',
              'subtitle',
              'technology',
              'thumbnail',
              'description',
              'image1',
              'image2',
              'image3',]
    
    list_display = ['name',]

admin.site.register(Website)