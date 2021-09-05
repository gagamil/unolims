from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from taggit.managers import TaggableManager


# Create your models here.
class Tube(models.Model):
    tube_id = models.CharField(max_length=30)


class TubeBatch(models.Model):
    tubes = models.ManyToManyField(Tube, through='TubeBatchPosition')
    title = models.CharField(max_length=100, blank=True)
    xtra_data = models.JSONField()
    tags = TaggableManager()


class TubeBatchPosition(models.Model):
    tube = models.ForeignKey(Tube, on_delete=models.PROTECT)
    batch = models.ForeignKey(TubeBatch, on_delete=models.PROTECT)
    position = models.CharField(max_length=3)