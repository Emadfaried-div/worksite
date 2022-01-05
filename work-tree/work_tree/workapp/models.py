from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings
from datetime import date
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
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
    ('UTILITIES','utilities'),
)

PO_CHOICES=(
    ('DELIVERED','delivered'),
    ('On_Way','on_way'),

)

Area_CHOICES=(
    ('BM3','BM3'),
    ('BM4','BM4'),
    ('BM5','BM5'),
    ('BM6','BM6'),
    ('CAP_Inj Nessie1','CAP_Inj Nessie1'),
    ('CAP_Inj Nessie2','CAP_Inj Nessie2'),
    ('CAP_Inj Arburg','CAP_Inj Arburg'),
    ('CAP_assempl','CAP_assempl'),
    ('BP360AMP','BP360AMP'),
    ('BP360LV','BP360LV'),
    ('BP460','BP460'),
    ('BP312','BP312'),
    ('Micro-lab','Micro-lab'),
    ('Micro-Chimical','Micro-Chimical'),
    ('BM-Piovan','BM-Piovan'),
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
    ('RS','RS'),
    ('NOORGREEN','NOORGREEN'),
    ('REXROTH','REXROTH'),
    ('TALAT_ELMASRY','TALAT_ELMASRY'),
    ("Ousuka-Techno","Ousuka-Techno"),
    ("Eltartosiah","Eltartosiah"),
    ("Bielomatic","Bielomatic"),
    ("Lubricant_Engineers","Lubricant_Engineers"),
    ("Omega","Omega"),
)


class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="admins",blank=True,null=True)
    mobile=models.CharField(max_length=20)
    def __str__(self):
        return self.user.username

class StoreCode(models.Model):
    short_item_no = models.CharField(max_length=200,blank=True,null=True)
    item_code = models.CharField(max_length=200,blank=True,null=True)
    description1= models.CharField(max_length=200,blank=True,null=True)
    description2= models.CharField(max_length=200,blank=True,null=True)
    Search_text = models.CharField(max_length=200,blank=True,null=True)
    Sp_Branch = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    g_l_cat = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return str(self.description1)


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
    visible_to = models.ManyToManyField(User, related_name="visible_to")
    editable_r = models.ManyToManyField(User, related_name="editable_r")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("oneoffer", kwargs={
            'slug': self.slug
        })
    def ImageUrl(self):
            if self.image:
                return self.image.url
            else:
               return ""

    def image_img(self):
        if self.image:
            return mark_safe('<img src="{}" heights="90" width="90" />'.format(self.image.url))
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'

class ThePo(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    store_code = models.CharField(max_length=200,blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    description = RichTextUploadingField()
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/%Y/%m/%D/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    show_to = models.ManyToManyField(User, related_name="show_to")
    edit_by = models.ManyToManyField(User, related_name="edit_by")
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)
    po_price= models.PositiveIntegerField(default=0,blank=True, null=True)
    po_status =models.CharField(max_length=200,choices=PO_CHOICES,default='on_way',blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("po_details", kwargs={
            'slug': self.slug
        })
    def image_img(self):
        if self.image:
            return mark_safe('<img src="{}" heights="90" width="90" />'.format(self.image.url))
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'


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
    description = RichTextUploadingField()
    area = models.CharField(max_length=100,choices=Area_CHOICES,default='Bp360AMP',blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    created_at = models.DateField(auto_now_add =True,blank=True,null=True)
    due_date  = models.DateField (blank=True,null=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='not-yet',blank=True,null=True)
    delete_obj=models.CharField(max_length=100,default='delete?',blank=True,null=True)
    update_obj=models.CharField(max_length=200,default='Edit?',blank=True,null=True)
    see_it_to = models.ManyToManyField(User, related_name="see_it_to")
    edit_it_by = models.ManyToManyField(User, related_name="edit_it_by")

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
    store_code = models.CharField(max_length=200,blank=True, null=True)
    offer=models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = True)
    dept  = models.CharField(max_length=200,blank=True, null=True)
    section=models.CharField(max_length=100,choices=SECTION_CHOICES,default='mechanical',blank=True,null=True)
    market= models.CharField(max_length=200,choices=MARKET_CHOICES,default='Local', blank=True,null=True)
    vendor = models.CharField(max_length=200,choices=VENDOR_CHOICES,default='?',blank=True, null=True)
    description =  RichTextField(blank=False, null=False)
    responseibilty = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    document = models.FileField(upload_to='Order-doc/',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    samples = models.CharField(max_length = 200 , blank=True, null=True)
    numbers_of_offers = models.PositiveIntegerField(default=1,blank=True, null=True)
    order_price= models.DecimalField(max_digits = 8, decimal_places = 2)
    order_status =models.CharField(max_length=200,choices=PO_CHOICES,default='on_way',blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    showing_to = models.ManyToManyField(User, related_name="showing_to")
    editing_by = models.ManyToManyField(User, related_name="editing_by")
    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse("oneorder", kwargs={
            'slug': self.slug
        })
    def image_img(self):
        if self.image:
            return mark_safe('<img src="{}" heights="90" width="90" />'.format(self.image.url))
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'



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



class Images(models.Model):
    po = models.ForeignKey(ThePo, on_delete=models.CASCADE,blank=True,null=True)
    offer= models.ForeignKey(TheOffer, on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(TheOrder, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title



class Jop_Order(models.Model):
    departement = models.CharField(max_length=50 ,blank=True,null=True)
    machine_id = models.CharField(max_length=50 ,blank=True,null=True)
    store_code = models.ForeignKey(StoreCode,on_delete=models.CASCADE,blank=True, null=True)
    date = models.DateField(_("Date"), auto_now_add=True)
    reporting_time = models.TimeField( blank=True,null=True)
    repair_start_time = models.TimeField( blank=True,null=True)
    repair_end_time = models.TimeField( blank=True,null=True)
    operator = models.CharField(max_length=50 ,blank=True,null=True)
    section_head = models.CharField(max_length=50 ,blank=True,null=True)
    noun_damage = models.CharField(max_length=1000 ,blank=True,null=True)
    possible_cause = models.CharField(max_length=1000 ,blank=True,null=True)
    repair_steps =  RichTextField(blank=False, null=False)
    used_spare_parts = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to= "products")
    job_order_image= models.ImageField(upload_to= "products")
    repairer = models.CharField(max_length=200,blank=True,null=True)
    responseble_eng = models.CharField(max_length=200,blank=True,null=True)
    slug = models.SlugField(unique = True)
    def __str__(self):
        return self.noun_damage

    def get_absolute_url(self):
        return reverse("one_jop", kwargs={
            'slug': self.slug
        })
    def image_img(self):
        if self.image:
            return mark_safe('<img src="{}" heights="90" width="90" />'.format(self.image.url))
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'



class KapasFollowUp(models.Model):
    capa_request_number = models.CharField(max_length=200, null=True, blank=True)
    capa_request_date = models.CharField(max_length=200, null=True, blank=True)
    source_reference_no = models.CharField(max_length=200, null=True, blank=True)
    finding_source_date = models.CharField(max_length=200, null=True, blank=True)
    finding_no = models.CharField(max_length=200, null=True, blank=True)
    finding_description = models.TextField(max_length=2000, null=True, blank=True)
    finding_category = models.CharField(max_length=20, null=True, blank=True)
    hosting_department = models.CharField(max_length=200, null=True, blank=True)
    capa = models.TextField(null=True, blank=True)
    due_date = models.CharField(max_length=200, null=True, blank=True)
    capa_s_responsible_department = models.CharField(max_length=200, null=True, blank=True)
    department_extra_comments = models.TextField( null=True, blank=True)
    compliance_extra_comments = models.CharField(max_length=200, null=True, blank=True)
    final_status = models.CharField(max_length=50, null=True, blank=True)
    source  = models.CharField(max_length=50, null=True, blank=True)
    justification_for_modification = models.CharField(max_length=200, null=True, blank=True)
    department_extra_comments = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.capa_request_number



