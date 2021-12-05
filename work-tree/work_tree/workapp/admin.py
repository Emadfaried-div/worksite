from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
import threading
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import (send_mail, BadHeaderError, EmailMessage)
from django.contrib.auth.models import User
from mptt.admin import DraggableMPTTAdmin
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class productImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

admin.site.register(MonthlyReport)
admin.site.register(DailyNotes)
admin.site.register(Images)
admin.site.register(MonthMenets)
admin.site.register(Admin)
admin.site.register(Customer)

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

class BroadCast_Email_Admin(admin.ModelAdmin):
    model = BroadCast_Email

    def submit_email(self, request, obj): #`obj` is queryset, so there we only use first selection, exacly obj[0]
        list_email_user = [ p.email for p in User.objects.all() ] #: if p.email != settings.EMAIL_HOST_USER   #this for exception
        obj_selected = obj[0]
        EmailThread(obj_selected.subject, mark_safe(obj_selected.message), list_email_user).start()
    submit_email.short_description = 'Submit BroadCast (200 Select Only)'
    submit_email.allow_tags = True

    actions = [ 'submit_email' ]

    list_display = ("subject", "created")
    search_fields = ['subject',]

admin.site.register(BroadCast_Email, BroadCast_Email_Admin)



class SendMail(admin.ModelAdmin):
    def send(self):
        self.send_mail= send_mail
        
        send_mail("Hello","Hello there. this is automated message!","nemhfa@gmail.com",["efaried@icloud.com"],fail_silently=False)
    
    
class ThePoAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'offer', 'title', 'image_img', 'vendor','date','quantity']  
    readonly_fields = ('image_img',)
    list_per_page = 10
    search_fields = ['title','vendor']
    inlines = [productImageInline]
    prepopulated_fields = {'slug': ('title',)}    
    
admin.site.register(ThePo,ThePoAdmin)    


class TheOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'offer', 'title', 'image_img', 'vendor','date','quantity'] 
    readonly_fields = ('image_img',)
    list_per_page = 10
    search_fields = ['title','vendor']
    inlines = [productImageInline]
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(TheOrder,TheOrderAdmin)      


 
    
 


    
    
class TheOfferAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'section', 'vendor','image_img','quantity','totalprice']  
    readonly_fields = ('image_img',)
    list_per_page = 10
    search_fields = ['title','vendor']
    inlines = [productImageInline]
    prepopulated_fields = {'slug': ('title',)} 
    
admin.site.register(TheOffer,TheOfferAdmin)   