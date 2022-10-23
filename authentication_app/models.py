from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

# Create your models here.




class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(blank=True,max_length=20)
	courntry = models.CharField(blank=True,max_length=200)
	city = models.CharField(blank=True,max_length=200)
	country = models.CharField(blank=True,max_length=200)
	

	def __str__(self):
		return self.user.username