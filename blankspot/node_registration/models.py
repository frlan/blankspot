from django.db import models

class position(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    altitude = models.FloatField()
    latitude = models.FloatField()
    
    def __unicode__(self):  
        return self.email
