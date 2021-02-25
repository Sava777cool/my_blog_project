from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateField(auto_now_add=True)
	post_image = models.ImageField(upload_to='post_image/')
	post_text = models.CharField(max_length=1000)