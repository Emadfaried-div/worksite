from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings

# Create your models here.
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "media/%s.%s"%(instance.id,extension)

MARKET_CHOICES=(
    ('LOCAL','Local'), 
    ('EXTERNAL','External'),
    
)

SECTION_CHOICES=(
    ('ELECTRICAL','electerical'),
    ('MECHANICAL','mechanical'),
    ('ELECTRICAL & MECHANICAL','electrical & mechanical'),
)


class TheOffer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    responseibilty = models.CharField(max_length=200)
    image_of_offer=models.ImageField(blank=True,null=True,upload_to= "products")
    image = models.ImageField(upload_to= "products")
    offer2_image2=models.ImageField(blank=True,null=True,upload_to= "products")
    offer3_image= models.ImageField(blank=True,null=True,upload_to= "products")
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    totalprice = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title



class ThePo(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor=models.CharField(max_length=200)
    description = models.TextField()
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)

    def __str__(self):
        return self.title  

    def __str__(self):
        return self.title        


class MonthlyReport(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True) 
    image = models.ImageField(upload_to= "products")
    
    def __str__(self):
        return self.title 
        






STATUS_CHOICES=(
    ('DONE','done'),
    ('NOT_YET','not-yet'),
)     

class DailyNotes(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    responsible=models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField()
    area = models.CharField(max_length=300,blank=True,null=True)
    vendor = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add =True,blank=True,null=True)   
    due_date  = models.DateTimeField(blank=True,null=True) 
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='not-yet',blank=True,null=True)
    delete_obj=models.CharField(max_length=100,default='delete?',blank=True,null=True)
    update_obj=models.CharField(max_length=200,default='Edit?',blank=True,null=True)
    def __str__(self):
        return self.description
    
    

        
        
class TheOrder(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    notes=models.ForeignKey(DailyNotes,on_delete=models.CASCADE,blank=True, null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor=models.CharField(max_length=200)
    description = models.TextField()
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)

    def __str__(self):
        return self.title        
    
    
    
class MonthMenets(models.Model):
    monthtitle=models.CharField(max_length=200,blank=True, null=True)
    task = models.CharField(max_length=200)
    
    def __str__(self):
        return self.task
    