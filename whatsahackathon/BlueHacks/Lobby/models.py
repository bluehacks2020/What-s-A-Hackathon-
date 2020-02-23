from django.db import models
from IndigenousPeople.models import CultureInfo


class Exhibition(models.Model):
    culture = models.ForeignKey(CultureInfo, on_delete=models.CASCADE)
    short_description = models.TextField()

    def __str__(self):
    	return "{}".format(self.culture.name)
