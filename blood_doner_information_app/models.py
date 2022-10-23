from dataclasses import fields
import email
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django import forms

# Create your models here.


class blood_doner_info(models.Model):
    name = models.CharField(blank=True,max_length=200)
    email = models.CharField(blank=True,max_length=30)
    phone=models.CharField(blank=True,max_length=20)
    blood_group = models.CharField(blank=True,max_length=200)
    gender = models.CharField(blank=True,max_length=200)
    age = models.CharField(blank=True,max_length=200)
    author= models.CharField(blank=True,max_length=100)
        

    def __str__(self):
        return self.name



#blood_doner_info_form
class blood_doner_createForm(ModelForm):
    class Meta:
        model = blood_doner_info
        fields = ['name', 'email', 'phone','age','gender','blood_group']



        
