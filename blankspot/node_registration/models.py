from django.db import models

class Position(models.Model):
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	nick = models.CharField(max_length=128)
	email = models.EmailField(max_length=254)
	street = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	address_description = models.TextField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)

	def __unicode__(self):
		knode = []
		if self.city:
			knode.append(self.city)
		if self.street:
			knode.append(self.street)
		if self.latitude:
			knode.append(str(self.latitude))
		if self.longitude:
			knode.append(str(self.longitude))
		return u', '.join(knode)

	def get_absolute_url(self):
		return reverse('position-detail', kwargs={'pk': self.pk})
