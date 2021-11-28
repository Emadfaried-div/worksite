from django.urls import path
from django.conf.urls.static import static
from . import views



urlpatterns = [
    
    
    path("", views.HomeView.as_view(), name= "home"),
    #path('orders/',views.orders,name='orders'),
    path("orders/",views.AllOrderstView.as_view(), name="orders"),
    path("one_order/<slug:slug>", views.OrderDetailView.as_view(), name= "oneorder"),
    #path('one_order/<int:id>', views.one_order,name='oneorder'),
    path('about', views.about,name='about'),
    #path('po/',views.po,name='po'),
    path("po/",views.AllPotView.as_view(), name="po"),
    #path('po_details/<int:id>',views.po_details,name='onepo'),
    path("po_details/<slug:slug>", views.PoDetailView.as_view(), name= "onepo"),
    ###path('report_create',views.report_create,name='report_create'),
    path("report_create/",views.ReportCreateView.as_view(), name="report_create"),
    #path('monthly_report',views.monthly_report,name='monthly_report'),
    path("monthly_report/",views.AllMonthlytView.as_view(), name="monthly_report"),
    #path('one_report/<int:id>',views.one_report,name='one_report'),
    path("one_report/<slug:slug>", views.ReportDetailView.as_view(), name= "one_report"),
    ###path('createnote',views.dailynotescreate,name='createnote'),
    path("createnote/",views.DailyNotesCreateView.as_view(), name="createnote"),
    ###path('daily_notes',views.daily_notes,name='daily_notes'),
    path("daily_notes/",views.DailyNotesView.as_view(), name="daily_notes"),
    #path('offer',views.offer, name='offer'),
    path("offer/",views.AllOfferstView.as_view(), name="offer"),
   # path('oneoffer/<int:id>',views.oneoffer,name='oneoffer'),
   path("oneoffer/<slug:slug>", views.OfferDetailView.as_view(), name= "oneoffer"),
    path('monthtasks',views.list_view,name='monthtasks'),
    path("search/",views.SearchView.as_view(),name="search"),
    path('delete/<int:id>',views.delete_view,name='delete'),
    path('update/<int:id>',views.update_view,name='update'),
    path('month_task_create',views.monthtasksform,name='month_task_create'),
    path("profile/",views.CustomerProfileView.as_view(), name="customerprofile"),
    path("register/",views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path("login/",views.CustomerLoginView.as_view(), name="login"),
    path("logout/",views.CustomerLogoutView.as_view(), name="customerlogout"),
    path("send/",views.send,name="send"),
]
