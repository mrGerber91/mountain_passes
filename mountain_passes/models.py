from django.db import models
from django.utils import timezone

class Users(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

class PerevalAdded(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.TextField()
    add_time = models.DateTimeField()
    winter_level = models.CharField(max_length=10)
    summer_level = models.CharField(max_length=10)
    autumn_level = models.CharField(max_length=10)
    spring_level = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default='new')

    class Meta:
        db_table = 'pereval_added'


class PerevalImages(models.Model):
    pereval_added = models.ForeignKey(PerevalAdded, related_name='images', on_delete=models.CASCADE)
    data = models.ImageField()
    title = models.CharField(max_length=100)

