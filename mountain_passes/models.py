from django.db import models

class PerevalAdded(models.Model):
    date_added = models.DateTimeField()
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.TextField()
    add_time = models.DateTimeField()
    winter_level = models.CharField(max_length=10)
    summer_level = models.CharField(max_length=10)
    autumn_level = models.CharField(max_length=10)
    spring_level = models.CharField(max_length=10)
    coord_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=20, default='new')


class PerevalImages(models.Model):
    title = models.CharField(max_length=100)

class Users(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)