from django.urls import path
from django.conf.urls.static import static
from maintenance.views import checklist, utilitychecklist,CheckListsearchSView,utilityCheckListsearchSView
from . import views

app_name= "maintenance"
urlpatterns = [
    path("checklist",views.checklist,name="checklist"),
    path("checklist_upload",views.checklist_upload,name= "checklist_upload"),
    path("utilitychecklist/",views.utilitychecklist,name="utilitychecklist"),
    path("utilitychecklist_upload/",views.utilitychecklist_upload,name= "utilitychecklist_upload"),
    path('lists',views.FolderCheckList, name="lists"),
    path("doc_srch/",views.CheckListsearchSView.as_view(), name="doc_srch"),
    path("utilitydoc_srch/",views.utilityCheckListsearchSView.as_view(), name="utilitydoc_srch"),
]