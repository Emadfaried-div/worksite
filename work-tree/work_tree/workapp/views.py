from django.db.models.query_utils import Q
from django.forms.forms import Form

from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse, request
from django.views.generic.base import TemplateView
from . import forms
from django.contrib.auth.models import User,AbstractUser
import sys
from . forms import TheOfferForm,Jop_OrderForm ,ThePoForm

from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.template.loader import get_template
from . models import *
from . models import StoreCode, KapasFollowUp
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . utils import render_to_pdf #created in step 4
from django.views.generic import ListView, TemplateView , DetailView , View, CreateView, FormView
#from ecomapp.utils import password_reset_token
from django.db.models import Sum
from django.urls import reverse_lazy
from datetime import datetime
from django.utils.crypto import get_random_string
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
TemplateView.as_view(extra_context={'order': 'order'})
from .utils import password_reset_token
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from templated_docs import fill_template
from templated_docs.http import FileResponse
from django.utils.translation import gettext as _
from django.core.paginator import Paginator
import PyPDF2
import io
import os
from io import BytesIO
from django.http import FileResponse
import csv
from .resources import KapasFollowUpResources, SotreCodeResources
from django.contrib import messages

from tablib import Dataset

class HomeView(LoginRequiredMixin,TemplateView):
    paginate_by= 12
    model=TheOrder

    template_name = "home.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        order=TheOrder.objects.all().order_by("-id")
     #   paginator = Paginator(all_products, 12)
     #   page_number = self.request.GET.get('page')
     #   product_list = paginator.get_page(page_number)
        context["order"]= order
        return context






#def po(request):
     #po=ThePo.objects.all().order_by("-id")
     #context={
          #'po':po
     #}
    # return render(request,'po.html',context)

class AllPotView(LoginRequiredMixin, TemplateView):
    template_name= "po.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["po"]= ThePo.objects.all().order_by("id")
        return context

#def po_details(request,id):
     #po=ThePo.objects.all()
     #one_po=ThePo.objects.get(id=id)

     #context ={
         # "one_po":one_po,
     # }
    # return render(request,"po_details.html",context)
class PoDetailView(LoginRequiredMixin, TemplateView):
    template_name= "po_details.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        one_po = ThePo.objects.get(slug=url_slug)
        one_po.view_count+=1
        one_po.save()
        context["one_po"] = one_po
        return context

#def monthly_report(request):
     #report=MonthlyReport.objects.all()
     #context={
         # 'report':report
     #}
    # return render(request,'monthly_report.html',context)

class AllMonthlytView(LoginRequiredMixin, TemplateView):
    template_name= "monthly_report.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["report"]= MonthlyReport.objects.all().order_by("id")
        return context


#def one_report(request,id):
    #one_report=MonthlyReport.objects.get(id=id)

     #context ={
         # "one_report":one_report,
         # }

    # return render(request,"one_report.html",context)


class ReportDetailView(LoginRequiredMixin, TemplateView):
    template_name= "one_report.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        one_report = MonthlyReport.objects.get(slug=url_slug)
        one_report.view_count+=1
        one_report.save()
        context["one_report"] = one_report
        return context


#def report_create(request):
     #if request.method == "POST":
         # form= forms.MonthlyReportForm(request.POST,request.FILES)
          #print (" have got a request")
          #if form.is_valid():
             #  instance =form.save(commit=False)
              # instance.author=request.user
              # instance.save()
              ## form.save()
              # print (form.cleaned_data,"5555555555555")
         # return redirect('monthly_report')

     #else:
         #form = forms.MonthlyReportForm()
     #return render(request,'create.html',{'form':form})

class ReportCreateView(LoginRequiredMixin, CreateView):
    template_name="create.html"
    form_class= forms.MonthlyReportForm
    success_url=reverse_lazy("monthly_report")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
           return redirect("login")

        return super().dispatch(request, *args, **kwargs)
        if request.method == "POST":
          form= forms.MonthlyReportForm(request.POST,request.FILES)
          print (" have got a request")
          if form.is_valid():
               instance =form.save(commit=False)
               instance.author=request.user
              #instance.save()
               form.save()
               print (form.cleaned_data,"5555555555555")
          return redirect('monthly_report')

        else:
         form = forms.MonthlyReportForm()
         return render(request,'create.html',{'form':form})






#def daily_notes(request):
    # daily_notes=DailyNotes.objects.all()
     #context={
          #'daily_notes':daily_notes,
    # }
    # return render(request,'daily_notes.html',context)
#class MyView( View):
   # permission_required = ('can_view_daily notes', 'can_delete_daily notes',"can_view_the_order")

class DailyNotesView(LoginRequiredMixin,TemplateView):
    template_name= "daily_notes.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["daily_notes"]= DailyNotes.objects.all().order_by("id")
        return context

#def dailynotescreate(request):
    # if request.method == "POST":
        #  form = forms.DialyNotesForm(request.POST,request.FILES)
         # print (" we have got  post ***************************************************")
         # if form.is_valid():
            # instance=form.save(commit=False)
            # instance.author=request.user
             #instance.save()
             #print(form.cleaned_data,instance,"111111111111111111111111111111111111")

          #return redirect ('daily_notes')

    # else:
         # form=forms.DialyNotesForm()

     #return render(request,"create_note.html",{'form':form})


class DailyNotesCreateView(LoginRequiredMixin, CreateView):
    template_name="create_note.html"
    form_class= forms.DialyNotesForm
    success_url=reverse_lazy("daily_notes")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
           return redirect("login")

        return super().dispatch(request, *args, **kwargs)
        if request.method == "POST":
              form = forms.DialyNotesForm(request.POST,request.FILES)
              print (" we have got  post ***************************************************")
              if form.is_valid():
                  instance=form.save(commit=False)
                  instance.author=request.user
                  instance.save()
                  print(form.cleaned_data,instance,"111111111111111111111111111111111111")

                  return redirect ('daily_notes')

        else:
          form=forms.DialyNotesForm()

        return render(request,"create_note.html",{'form':form})


@login_required
# delete view for details
#@permission_required('can_view_daily_notes', raise_exception=True)
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys


    # fetch the object related to passed id
    obj = get_object_or_404(DailyNotes, id = id)
    context ={'obj':obj}

    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        send_mail(
            subject="The notes has been deleted",
            message="dialy note  has been deleted successfuly;",
            from_email="nemhfa@gmail.com",
            recipient_list=["nemhfa@gmail.com"]
        )
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

@login_required
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(DailyNotes, id = id)

    # pass the object as instance in form
    form = forms.DialyNotesForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        send_mail(
            subject="The notes has been updated",
            message="dialy note  has been updated successfuly;",
            from_email="nemhfa@gmail.com",
            recipient_list=["nemhfa@gmail.com"]
        )
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


#def offer(request):
   #  offer = TheOffer.objects.all().order_by("-id")
     #context = {
    #      'offer':offer,
    # }
    # return render(request,'offers.html',context)
class AllOfferstView(LoginRequiredMixin, TemplateView):
    template_name= "offers.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["offer"]= TheOffer.objects.all().order_by("id")
        return context

class TheOfferCreateView(LoginRequiredMixin, CreateView):
    template_name="create_offer.html"
    form_class= forms.TheOfferForm
    success_url=reverse_lazy("offer")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
           return redirect("login")

        return super().dispatch(request, *args, **kwargs)
        if request.method == "POST":
              form = forms.TheOfferForm(request.POST,request.FILES)
              print (" we have got  post ***************************************************")
              if form.is_valid():
                  instance=form.save(commit=False)
                  instance.author=request.user
                  instance.save()
                  print(form.cleaned_data,instance,"111111111111111111111111111111111111")

                  return redirect ('create_offer')

        else:
          form=forms.TheOfferForm()

        return render(request,"create_offer.html",{'form':form})


#def oneoffer(request,id):
     #oneoffer = TheOffer.objects.get(id=id)
     #context = {
          #'oneoffer':oneoffer,
     #}

    #return render(request,'oneoffer.html',context)
class OfferDetailView(LoginRequiredMixin, TemplateView):
    template_name= "oneoffer.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        one_offer = TheOffer.objects.get(slug=url_slug)
        one_offer.view_count+=1
        one_offer.save()
        context["one_offer"] =  one_offer
        return context

#def orders(request):
     #order = TheOrder.objects.all().order_by("-id")

     #context={

         # 'order':order,
     #}
    # return render (request,'orders_po.html',context)
class AllOrderstView(LoginRequiredMixin,TemplateView):
    template_name= "orders_po.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        order= TheOrder.objects.all().order_by("id")
        items = TheOrder.objects.all()
        total_price =sum(items.values_list('order_price',flat=True))

        context={
            "order":order,
            "total_price":total_price,
            }
        return context

#def one_order(request,id):
     #order = TheOrder.objects.all()
     #one_order=TheOrder.objects.get(id=id)

     #context ={
         # "one_order":one_order,
        # }

     #return render(request,"order_details.html",context)

class TheOrderCreateView(LoginRequiredMixin, CreateView):
    template_name="create_order.html"
    form_class= forms.TheOrderForm
    success_url=reverse_lazy("orders")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
           return redirect("login")

        return super().dispatch(request, *args, **kwargs)
        if request.method == "POST":
              form = forms.TheOfferForm(request.POST,request.FILES)
              print (" we have got  post ***************************************************")
              if form.is_valid():
                  instance=form.save(commit=False)
                  instance.author=request.user
                  instance.save()
                  print(form.cleaned_data,instance,"111111111111111111111111111111111111")

                  return redirect ('create_order')

        else:
          form=forms.TheOfferForm()

        return render(request,"create_order.html",{'form':form})


class OrderDetailView(LoginRequiredMixin, TemplateView):
    template_name= "order_details.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        one_order = TheOrder.objects.get(slug=url_slug)
        one_order.view_count+=1
        one_order.save()
        context["one_order"] =  one_order
        return context


class SearchView(TemplateView):
    model = ThePo
    template_name="search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        results=ThePo.objects.filter(Q(title__icontains=kw)|Q(description__icontains=kw)|Q(vendor__icontains=kw)|Q(dept__icontains=kw) )
        search = DailyNotes.objects.filter(Q(area__icontains=kw)|Q(description__icontains=kw)|Q(vendor__icontains=kw)|Q(status__icontains=kw) )
        context["results"]=results
        return context


class CustomerRegistrationView(CreateView):
    template_name="customerregistration.html"
    form_class = forms.CustomerRegistrationForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get('password')
        email= form.cleaned_data.get("email")
        user=User.objects.create_user(username,email,password) # for here only customer created not user, to create user follow step line202
        form.instance.user= user
        login(self.request, user)
        return super().form_valid(form)
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url=self.request.GET.get("next")
            return next_url
        else:
            return self.success_url



#def login_view(request):
#    if request.method == "POST":
        #form = AuthenticationForm(data=request.POST)
       # print("we have login post")
       # if form.is_valid():
        #   user=form.get_user()

           # login(request, user)


          #  print(form.cleaned_data,"login form successfully")

           # return redirect('home')
    #else:
      #  form = AuthenticationForm()
       # return render (request,'login.html',{'form':form})


class CustomerLoginView(FormView):
    template_name="registration/login.html"
    form_class = forms.CustomerloginForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        uname=form.cleaned_data.get("username")
        pword=form.cleaned_data["password"]
        usr=authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name, {"form":self.form_class, "error":"Invaild Credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url=self.request.GET.get("next")
            return next_url
        else:
            return self.success_url





class CustomerLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")



@login_required

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = MonthMenets.objects.all()

    return render(request, "monthtasks.html", context)


class MonthTaskView(ListView):
    model = MonthMenets
    tmeplate_name = "monthtasks.html"
def month_task_pdf_view(request,*args,**kwargs):
    context ={}
    context["dataset"] = MonthMenets.objects.all()
    template_path = 'monthtasks.html'
    context["dataset"] = MonthMenets.objects.all()
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="month_tasks_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




@login_required
def monthtasksform(request):
     if request.method=='POST':
          form = forms.MonthTasksForm(request.POST,request.FILES)
          if form.is_valid():
               instance=form.save(commit=False)
               instance.author = request.user
               instance.save()
               return redirect('monthtasks')
     else:
          form = forms.MonthTasksForm()
     return render (request,'month_task_create.html',{'form':form})



class CustomerProfileView(TemplateView):
    template_name="customerprofile.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
           return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        customer= self.request.user.customer

        orders=TheOrder.objects.all()
        pos = ThePo.objects.all()
        items = TheOrder.objects.all()
        total_price =sum(items.values_list('order_price',flat=True))
        prices =ThePo.objects.all()
        all_prices = sum(prices.values_list('po_price',flat=True))
        context={
            "orders":orders,
            "pos":pos,
            "total_price":total_price,
            "all_prices":all_prices,
            }
        context["customer"]=customer
        return context





def about(request):
    return HttpResponse("<h1>About page<h1/>")


@login_required
def send_message(request):
    pass

    return redirect(request,"home.html")


def send(request):
        send_mail("Hello","Hello there. this is automated message!","nemhfa@gmail.com",["efaried@icloud.com"],fail_silently=False)
        return (request,"send_email.hmtl")






def dailynotes_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename= dailynotes.txt'

    notes = DailyNotes.objects.all()
    lines =[]
    for note in notes :
        lines.append(f'id={note.id}\ndescription:-{note.description}\nvendor:-{note.vendor}\ndue_date:{note.due_date}\nstatus:-{note.status}\n\n\n')
    response.writelines(lines)
    return response

def monthtasks_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= Monthtasks.csv'
    #create a csv writer
    writer = csv.writer(response)

    tasks = MonthMenets.objects.all()

    #add column headings to csv file
    writer.writerow([ 'task_date', 'task' , 'area'])
    for task in tasks :
        writer.writerow([ task.task_date , task.task , task.area ])
    return response

def simple_upload(request):
    if request.method == 'POST':
        storecode_resource = SotreCodeResources()
        dataset = Dataset

        new_code = request.FILES['item location']
        if not new_code.name.endswith('xlsx'):
            message.info(request,'wrong format')
            return render(request,'code_upload.html')

        imported_data = dataset.load(new_code.read(),format='xlsx')
        for data in imported_data:

        	value = StoreCode(
        	    data[4],
        	)
        	value.save()
    items =  StoreCode.objects.all()
    context = {
        'items': items
        }
    return render(request,'code_upload.html',context)



class CodeSearchView(TemplateView):
    model = StoreCode
    template_name="Code_search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        codes=StoreCode.objects.filter(Q(short_item_no__icontains=kw)|Q(description1__icontains=kw)|Q(description2__icontains=kw) )

        context["codes"]=codes
        return context


class Jop_OrderView(LoginRequiredMixin,TemplateView):
    template_name= "job_order.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["jobs"]= Jop_Order.objects.all().order_by("id")
        return context


class jobOrderDetailView(LoginRequiredMixin, TemplateView):
    template_name= "job_order_details.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        one_jop = Jop_Order.objects.get(slug=url_slug)


        context["one_jop"] =  one_jop
        return context


class ThePoSearchSView(TemplateView):
    model =ThePo
    template_name="po_search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        pos = ThePo.objects.filter(Q(title__icontains=kw)|Q(description__icontains=kw)|Q(vendor__icontains=kw) )

        context["pos"]=pos
        return context


@login_required
def Jop_OrderForm(request):
     if request.method=='POST':
          form = forms.Jop_OrderForm(request.POST,request.FILES)
          if form.is_valid():
               instance=form.save(commit=False)
               instance.author = request.user
               instance.save()
               return redirect('job_order')
     else:
          form = forms.Jop_OrderForm()
     return render (request,'job_order_create.html',{'form':form})


@login_required
def ThePoForm(request):
     if request.method=='POST':
          form = forms.ThePoForm(request.POST,request.FILES)
          if form.is_valid():
               instance=form.save(commit=False)
               instance.author = request.user
               instance.save()
               return redirect('po')
     else:
          form = forms.ThePoForm()
     return render (request,'po_create.html',{'form':form})

class TheOrdersearchSView(TemplateView):
    model =TheOrder
    template_name="order_search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        orders = TheOrder.objects.filter(Q(title__icontains=kw)|Q(description__icontains=kw)|Q(vendor__icontains=kw)|Q(market__icontains=kw))

        context["orders"]=orders
        return context


class TheOffersearchSView(TemplateView):
    model =TheOffer
    template_name="offer_search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        offers = TheOffer.objects.filter(Q(title__icontains=kw)|Q(section__icontains=kw)|Q(vendor__icontains=kw)|Q(market__icontains=kw))

        context["offers"]=offers
        return context


class Jop_OrderrsearchSView(TemplateView):
    model =Jop_Order
    template_name="jop_order_search.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        jobs = Jop_Order.objects.filter(Q(departement__icontains=kw)|Q(machine_id__icontains=kw)|Q(noun_damage__icontains=kw)|Q(repair_steps__icontains=kw))

        context["jobs"]=jobs
        return context
    
def shutdown_plan(request):
    
    return render(request,"shutdown_maintenance.html")    


def kapas_upload(request):
    if request.method == 'POST':
        storecode_resource = KapasFollowUpResources()
        dataset = Dataset

        new_code = request.FILES['kapa follow up']
        if not new_code.name.endswith('xlsx'):
            message.info(request,'wrong format')
            return render(request,'kapa_upload.html')

        imported_data = dataset.load(new_kapa.read(),format='xlsx')
        for data in imported_data:

        	value = KapasFollowUp(
        	    data[4],
        	)
        	value.save()
    items =  KapasFollowUp.objects.all()
    context = {
        'items': items
        }
    return render(request,'kapa_upload.html',context)