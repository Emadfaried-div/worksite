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

class Calendar(models.Model):
    calendar_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visible_for = models.ManyToManyField(User, related_name="visible_for")
    editable_by = models.ManyToManyField(User, related_name="editable_by")

    def __str__(self):
        return self.name

class Event(models.Model):
    TYPE_CHOICES = [
        ("WR", 'work'),
        ("OT", 'audit'),
        ("MT", 'maintenance'),
        
    ]
    event_id = models.AutoField(primary_key=True)
    calendar_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True,blank=True)
    event_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default="maintenance")

    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
