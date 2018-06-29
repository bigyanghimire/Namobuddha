from django.db import models
from datetime import datetime


# Create your models here.
class File(models.Model):

	
    
	title=models.CharField(max_length=200)
	document=models.FileField()
	comments=models.TextField()
	uploaded_at=models.DateTimeField(default=datetime.now,blank=True)
	category=models.CharField(max_length=200,default="Education")
	


	def __str__(self):
		return self.title
