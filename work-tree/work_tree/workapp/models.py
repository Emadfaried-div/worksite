from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings
from datetime import date
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _

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

Area_CHOICES=(
    ('BM3','BM3'),
    ('BM4','BM4'),
    ('BM5','BM5'),
    ('BM6','BM6'),
    ('CAP_Inj','CAP_Inj'),
    ('CAP_assempl','CAP_assempl'),
    ('BP360AMP','BP360AMP'),
    ('BP360LV','BP360LVt'),
    ('BP460','BP460'),
    ('BP312','BP312'),
)  


VENDOR_CHOICES=(
    ('Rommelag','Rommelag'),
    ('HENSE','HENSE'),
    ('ANGEPOT','ANGEPOT'),
    ('M_RASHAD','M_RASHAD'),
    ('HYDRAYLIC_SYSTEM','HYDRAYLIC_SYSTEM'),
    ('ELFARES','ELFARES'),
    ('ABO_ELILAA','ABO_ELILAA'),
    ('NEW_STAR_MOULD','NEW_STAR_MOULD'),
    ('ITALIX','ITALIX'),
    ('FESTO','FESTO'),
    ('SMC','SMC'),
    ('NOORGREEN','NOORGREEN'),
    ('REXROTH','REXROTH'),
    ('TALAT_ELMASRY','TALAT_ELMASRY'),
)  
class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="admins",blank=True,null=True)
    mobile=models.CharField(max_length=20)
    def __str__(self):
        return self.user.username


class TheOffer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = False)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    responseibilty = models.CharField(max_length=200)
    image_of_offer=models.ImageField(blank=True,null=True,upload_to= "products")
    image = models.ImageField(upload_to= "products")
    offer2_image2=models.ImageField(blank=True,null=True,upload_to= "products")
    offer3_image= models.ImageField(blank=True,null=True,upload_to= "products")
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    totalprice = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("oneoffer", kwargs={
            'slug': self.slug
        }) 

class ThePo(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor= models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    description = models.TextField()
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse("po_details", kwargs={
            'slug': self.slug
        })         


class MonthlyReport(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True) 
    image = models.ImageField(upload_to= "products")
    view_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title 
        
    def get_absolute_url(self):
        return reverse("one_report", kwargs={
            'slug': self.slug
        }) 





STATUS_CHOICES=(
    ('DONE','done'),
    ('NOT_YET','not-yet'),
)     

class DailyNotes(models.Model):
    class Meta:
        
        permissions = (("can_view_daily notes", "can_view_month menets"),)
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    responsible=models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField()
    area = models.CharField(max_length=100,choices=Area_CHOICES,default='?',blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    created_at = models.DateField(auto_now_add =True,blank=True,null=True)   
    due_date  = models.DateField (blank=True,null=True) 
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='not-yet',blank=True,null=True)
    delete_obj=models.CharField(max_length=100,default='delete?',blank=True,null=True)
    update_obj=models.CharField(max_length=200,default='Edit?',blank=True,null=True)
    
    def __str__(self):
        return self.description
    
    @property
    def is_overdue(self):
        if self.due_date and date.today() > self.due_date:
           return True
        return False

        
        
class TheOrder(models.Model):
    
    user= models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    notes=models.ForeignKey(DailyNotes,on_delete=models.CASCADE,blank=True, null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = True)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    description = models.TextField()
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse("oneorder", kwargs={
            'slug': self.slug
        })      
    
    
  
class MonthMenets(models.Model):
    task_date=models.CharField(max_length=200,blank=True, null=True)
    task = models.CharField(max_length=200)
    area = models.CharField(max_length=100,choices=Area_CHOICES,default='Bp360AMP',blank=True,null=True)
    def __str__(self):
        return self.task
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 200) 
    address = models.CharField(max_length = 200 , blank=True, null=True) 
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name    
    
    

        

class BroadCast_Email(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    message = RichTextField(blank=False, null=False)

    
    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "BroadCast Email to all Member"
        verbose_name_plural = "BroadCast Email"