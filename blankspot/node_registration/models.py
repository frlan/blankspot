from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	nick = models.CharField(max_length=128)
	email = models.EmailField(max_length=254)	
	
	def __unicode__(self):
		return (self.nick)

	def get_absolute_url(self):
		return reverse('contact-detail', kwargs={'pk': self.pk})

class Position(models.Model):
	contact = models.ForeignKey('Contact')
	street = models.CharField(max_length=200, blank=True, default="leer")
	city = models.CharField(max_length=100, blank=True, default="Jena")
	address_description = models.TextField(blank=True)
	altitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null= True)

	def __unicode__(self):
		return (self.street)

	def get_absolute_url(self):
		return reverse('position-detail', kwargs={'pk': self.pk})
