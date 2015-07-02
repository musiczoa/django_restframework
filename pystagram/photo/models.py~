# coding: utf-8

from django.db import models

class Photo(models.Model):
    #image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    image_file = models.ImageField()
    #filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    filtered_image_file = models.ImageField()
    description = models.TextField(max_length=500, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_at = models.DateTimeField()
