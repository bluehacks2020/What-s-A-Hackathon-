from django.db import models


class Product1(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
    price = models.IntegerField()

    def __str__(self):
    	return "{}".format(self.name)

class Product2(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
    price = models.IntegerField()


    def __str__(self):
        return "{}".format(self.name)

class Product3(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
    price = models.IntegerField()


    def __str__(self):
        return "{}".format(self.name)


class CultureInfo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url = models.CharField(max_length=2083)
    webpage = models.CharField(max_length=30)
    pic1 = models.CharField(max_length=2083)
    pic2 = models.CharField(max_length=2083)
    pic3 = models.CharField(max_length=2083)


    def __str__(self):
        return "{}".format(self.name)