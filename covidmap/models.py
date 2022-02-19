from django.db import models
from django.contrib.gis.db.models import PointField


# Create your models here.
class Covidinfor(models.Model):
    country = models.TextField(db_column='Country', blank=True, null=True,max_length=20)  # Field name made lowercase.
    totalcases = models.TextField(db_column='TotalCases', blank=True, null=True,max_length=20)  # Field name made lowercase.
    newcases = models.TextField(db_column='NewCases', blank=True, null=True,max_length=20)  # Field name made lowercase.
    totaldeaths = models.TextField(db_column='TotalDeaths', blank=True, null=True,max_length=20)  # Field name made lowercase.
    newdeaths = models.TextField(db_column='NewDeaths', blank=True, null=True,max_length=20)  # Field name made lowercase.
    totalrecovered = models.TextField(db_column='TotalRecovered', blank=True, null=True,max_length=20)  # Field name made lowercase.
    newrecovered = models.TextField(db_column='NewRecovered', blank=True, null=True,max_length=20)  # Field name made lowercase.
    activecases = models.TextField(db_column='ActiveCases', blank=True, null=True,max_length=20)  # Field name made lowercase.
    seriouscritical = models.TextField(db_column='SeriousCritical', blank=True, null=True,max_length=20)  # Field name made lowercase.
    totcases_1m_pop = models.TextField(db_column='TotCases_1M_pop', blank=True, null=True,max_length=20)  # Field name made lowercase.
    deaths_1m_pop = models.TextField(db_column='Deaths_1M_pop', blank=True, null=True,max_length=20)  # Field name made lowercase.
    totaltests = models.TextField(db_column='TotalTests', blank=True, null=True,max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.country 


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = PointField()