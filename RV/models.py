from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    cast = models.CharField(max_length=500)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters')

class User_register(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Reviews(models.Model):
    movie_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    review = models.CharField(max_length=500)


