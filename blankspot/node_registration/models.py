from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Position(models.Model):
	first_name = models.CharField(verbose_name=_("First Name"), max_length=50, blank=True, null=True)
	last_name = models.CharField(verbose_name=_("Family Name"), max_length=50, blank=True, null=True)
	nick = models.CharField(verbose_name=_("Nick*"), max_length=128)
	email = models.EmailField(verbose_name=_("E-mail*"), max_length=254)
	street = models.CharField(verbose_name=_("Street"), max_length=200, blank=True, null=True)
	city = models.CharField(verbose_name=_("City"), max_length=100, blank=True, null=True)
	address_description = models.TextField(verbose_name=_("Adressdescription"),
		help_text=_("A more detailed description of a possible  position. E.g. roof top with view over city to the south"),
		blank=True,
		null=True)
	longitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)

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
		return reverse('position-list')

	class Meta:
		verbose_name = _(u'Position')
		verbose_name_plural = _(u'Positions')
