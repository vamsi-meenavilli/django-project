from django.db import models

# Create your models here.
class registration(models.Model):
	username=models.CharField(max_length=25)
	email=models.CharField(max_length=25)
	mobile=models.CharField(max_length=10)
	profile_pic=models.FileField()

	def __str__(self):
		return self.username