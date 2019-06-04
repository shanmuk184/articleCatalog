from django.db import models

# Create your models here.

class Article(models.Model):
    job_id = models.IntegerField()
    ns_category_id = models.IntegerField()
    location_id = models.IntegerField()
    job_type_id = models.IntegerField()
    filename = models.CharField(max_length=100, blank=True,null=True)
    job_title = models.TextField(blank=True,null=True)
    job_slug = models.TextField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_image = models.TextField(blank=True, null=True)
    job_status = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    House_of = models.CharField(max_length=100, blank=True, null=True)
    Year = models.CharField(max_length=40,blank=True, null=True)
    epaperlink = models.TextField(blank=True, null=True)
    imagelink = models.TextField(blank=True, null=True)
    imagelinkautogenerate = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        db_table='articles'

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = ''