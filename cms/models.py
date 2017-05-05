from django.db import models


class Book(models.Model):
    name = models.CharField('Name', max_length=255)
    publisher = models.CharField('Publisher', max_length=255, blank=True)
    page = models.IntegerField('PageNum', blank=True, default=0)

    def __unicode__(self):
        return self.name


class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name='Book', related_name='impressions')
    comment = models.TextField('Comment', blank=True)

    def __unicode__(self):
        return self.comment