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


