from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

class Dream(models.Model):
	image = models.ImageField(upload_to=upload_to, blank=False, null=False)
	style = models.CharField(max_length=2, blank=False, null=False)


	def __str__(self):
		return self.title
