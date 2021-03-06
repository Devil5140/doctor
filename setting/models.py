from django.db import models

# Create your models here.
class Site_Configuration(models.Model):
	sitename = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='logo')
	email = models.EmailField(max_length=100)
	contact= models.CharField(max_length=20)
	facebooklink=models.CharField(max_length=100)
	twitterlink=models.CharField(max_length=100)
	googlepluslink=models.CharField(max_length=100)
	
	
	def __str__(self):
		return self.sitename
		

class Banner(models.Model):
	bannername=models.CharField(max_length=100)
	banner = models.ImageField(upload_to='banner')
	homebanner=models.ImageField(upload_to='banner')
	symptombanner=models.ImageField(upload_to='banner')
	doctorbanner=models.ImageField(upload_to='banner')
	hospitalbanner=models.ImageField(upload_to='banner')
	locationbanner=models.ImageField(upload_to='banner')
	contactbanner=models.ImageField(upload_to='banner')
	def __str__(self):
		return self.bannername

class Footer(models.Model):
	Imagename=models.CharField(max_length=100)
	footerimage = models.ImageField(upload_to='footer')
	
	def __str__(self):
		return self.Imagename
			
		
