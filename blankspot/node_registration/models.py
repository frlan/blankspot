from django.db import models

class position(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	nick = models.CharField(max_length=128, null=True)
	email = models.EmailField(max_length=254)
	street = models.CharField(max_length=200, null=False, default="leer")
	city = models.CharField(max_length=100, null=True, default="Jena")
	address_description = models.TextField(null=True)
	altitude = models.FloatField()
	latitude = models.FloatField()

	def __unicode__(self):
		return (self.street)
