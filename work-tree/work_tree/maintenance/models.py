from django.db import models

# Create your models here.



class CheckList(models.Model):
    title = models.CharField(max_length=200)
    check_document= models.FileField(upload_to="check_list/docx/%Y/%m/%D/")
    def __str__(self):
        return self.title

class UtilityCheckList(models.Model):
    title1 = models.CharField(max_length=200)
    utilitycheck_document= models.FileField(upload_to="utilitychecklist/docx/%Y/%m/%D/")
    def __str__(self):
        return self.title1


class MaintenancePlan(models.Model):
    calendar_name = models.CharField(max_length=55)
    event_name = models.CharField(max_length=55)
    jan = models.name = models.CharField(max_length=2)
    feb = models.name = models.CharField(max_length=2)
    mar = models.name = models.CharField(max_length=2)
    apr = models.name = models.CharField(max_length=2)
    may = models.name = models.CharField(max_length=2)
    jun = models.name = models.CharField(max_length=2)
    jul = models.name = models.CharField(max_length=2)
    aug = models.name = models.CharField(max_length=2)
    sep = models.name = models.CharField(max_length=2)
    oct = models.name = models.CharField(max_length=2)
    nov = models.name = models.CharField(max_length=2)
    dec = models.name = models.CharField(max_length=2)
    
    def __str__(self):
        return self.calendar_name
