from django.db import models

# Create your models here.
class NoinfoDetail(models.Model):
    theme = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    form = models.CharField(max_length=100, blank=True, null=True)
    dim = models.CharField(max_length=100, blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    episode_start = models.IntegerField(blank=True, null=True)
    episode_end = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_watch_start = models.DateField(blank=True, null=True)
    date_watch_end = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noinfo_detail'