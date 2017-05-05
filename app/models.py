from django.db import models


class Corp(models.Model):
    name = models.CharField('Name', max_length=255)
    address = models.CharField('Address', max_length=255, blank=True)
    tel = models.IntegerField('Tel', blank=True, default=0)

    def __unicode__(self):
        return self.name
