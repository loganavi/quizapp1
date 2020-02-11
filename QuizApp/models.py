from django.db import models

# Create your models here.
class contact_form(models.Model):
	Name=models.CharField(max_length=255)
	Email=models.EmailField(max_length=255)
	Subject=models.CharField(max_length=255)
	Message=models.TextField()

class task(models.Model):
	answer=models.TextField()

	def __str__(self):
		return f'{self.answers}'