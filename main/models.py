from django.db import models


class photos(models.Model):
    image = models.ImageField(upload_to='media/images')
    desc = models.CharField(max_length=100)
