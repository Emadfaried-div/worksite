from django.db.models.query_utils import Q
from django.forms.forms import Form
from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse, request
from django.views.generic.base import TemplateView
from . import forms
from django.contrib.auth.models import User,AbstractUser
import sys
from . models import *
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.






def home(request):
     order=TheOrder.objects.all()
     context={
          'order':order,
     }
     return render(request,'home.html',context)


def po(request):
     po=ThePo.objects.all().order_by("-id")     
     context={
          'po':po
     } 
     return render(request,'po.html',context)


def po_details(request,id):
     po=ThePo.objects.all()
     one_po=ThePo.objects.get(id=id)
     
     context ={
          "one_po":one_po,
      }
     return render(request,"po_details.html",context)


def monthly_report(request):
     report=MonthlyReport.objects.all()
     context={
          'report':report
     }
     return render(request,'monthly_report.html',context)


def one_report(request,id):
     one_report=MonthlyReport.objects.get(id=id)
     
     context ={
          "one_report":one_report,
          }
     
     return render(request,"one_report.html",context)


def report_create(request):
     if request.method == "POST":
          form= forms.MonthlyReportForm(request.POST,request.FILES)
          print (" have got a request")
          if form.is_valid():
               instance =form.save(commit=False)  
               instance.author=request.user
               instance.save()
               form.save()
               print (form.cleaned_data,"5555555555555")   
          return redirect('monthly_report')     
               
     else:
         form = forms.MonthlyReportForm()
     return render(request,'create.html',{'form':form})


def daily_notes(request):
     daily_notes=DailyNotes.objects.all()
     context={
          'daily_notes':daily_notes,
     }
     return render(request,'daily_notes.html',context)



def dailynotescreate(request):
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


# delete view for details
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
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)
     

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
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)


def offer(request):
     offer = TheOffer.objects.all().order_by("-id")
     context = {
          'offer':offer,
     }
     return render(request,'offers.html',context)


def oneoffer(request,id):
     oneoffer = TheOffer.objects.get(id=id)
     context = {
          'oneoffer':oneoffer,
     }
     
     return render(request,'oneoffer.html',context)


def orders(request):
     order = TheOrder.objects.all().order_by("-id")
    
     context={
          
          'order':order,
     }
     return render (request,'orders_po.html',context)        


def one_order(request,id):
     order = TheOrder.objects.all()
     one_order=TheOrder.objects.get(id=id)
     
     context ={
          "one_order":one_order,
         }
    
     return render(request,"order_details.html",context)



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
   

def signup (request):
    if request.method == "POST":   
        form = UserCreationForm(request.POST)
        print("we have got a post request, 11111111111111111111111111111111111111")
        if form.is_valid():
            user=form.save( )
            login(request,user)
            
            print (form.cleaned_data,"22222222222222")
            
            return redirect("login")
        
    else:
        form =  UserCreationForm()
    return render(request,'signup.html',{'form':form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print("we have login post")
        if form.is_valid():
            user=form.get_user()
          
            login(request, user)
          
            
            print(form.cleaned_data,"login form successfully")
           
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render (request,'login.html',{'form':form})



@login_required
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('logged_out')
    return render( request,'logged_out.html')




def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = MonthMenets.objects.all()
         
    return render(request, "monthtasks.html", context)


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


def about(request):
    return HttpResponse("<h1>About page<h1/>")    