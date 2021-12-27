from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from maintenance.forms import CheckListForm, UtilityCheckListForm
from maintenance.models import CheckList, UtilityCheckList
from multiprocessing import context
from django.views.generic import ListView, TemplateView , DetailView , View, CreateView, FormView
from django.db.models.query_utils import Q
# Create your views here.


def FolderCheckList(request):
    utility_list="Engineering utilities list"
    plastizing_list="Mechanical List"
    context={
        'utility_list':utility_list,
        'plastizing_list':plastizing_list
        }
    return render(request,"maintenance/lists.html",context)


def checklist(request):
    lists=CheckList.objects.all()
    context={
        'lists':lists
    }
    return render (request,"maintenance/checklist.html",context)

def checklist_upload(request):
    if request.method == "POST":
        form = CheckListForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("maintenance:checklist")
    else:
        form = CheckListForm()
    return render(request,"maintenance/checkupload.html",{'form':form})


def utilitychecklist(request):
    utilitylist = UtilityCheckList.objects.all()
    context={
        'utilitylist':utilitylist
            }
    return render(request,"maintenance/utilitychecklist.html",context)


def utilitychecklist_upload(request):
    if request.method == "POST":
        form1 = UtilityCheckListForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect("maintenance:utilitychecklist")
    else:
        form1 = UtilityCheckListForm()
    return render(request,"maintenance/utilitycheckupload.html",{'form1':form1})




class CheckListsearchSView(TemplateView):
    model =CheckList
    template_name="maintenance/checklist.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        searchlist = CheckList.objects.filter(Q(title__icontains=kw)|Q(check_document__icontains=kw))

        context["searchlist"]=searchlist
        return context


class utilityCheckListsearchSView(TemplateView):
    model =UtilityCheckList
    template_name="maintenance/utilitychecklist.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        kw=self.request.GET.get("keyword")
        utilitysearchlist = UtilityCheckList.objects.filter(Q(title1__icontains=kw)|Q(utilitycheck_document__icontains=kw))

        context["utilitysearchlist"]=utilitysearchlist
        return context
