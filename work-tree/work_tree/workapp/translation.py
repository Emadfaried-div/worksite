
from modeltranslation.translator import register, translator, TranslationOptions
from .models import ContactMessage





class ContactMessageTranslationOptions(TranslationOptions):
    fields = ('name', 'email','subject','message','note','created_at')



translator.register(ContactMessage, ContactMessageTranslationOptions)    