from django.db import models

# Create your models here.


class Hotels(models.Model):

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="static/upload")
    location = models.CharField(max_length=30)
    rating = models.IntegerField()
    price = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    is_feature = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Blog(models.Model):

    mainhead = models.CharField(max_length=30)
    head = models.CharField(max_length=30)
    date = models.DateField()
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/upload")
    def __str__(self):
        return self.mainhead


