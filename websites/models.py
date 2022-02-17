from django.db import models


class Website(models.Model):
    name = models.CharField(null=False, blank=False, max_length=32)
    subtitle = models.CharField(null=False, blank=False, max_length=32)
    url = models.CharField(null=False, blank=False, max_length=128)
    thumbnail = models.ImageField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image1 = models.ImageField(null=False, blank=False)
    image2 = models.ImageField(null=False, blank=False)
    image3 = models.ImageField(null=False, blank=False)

    def __str__(self):
            return self.name