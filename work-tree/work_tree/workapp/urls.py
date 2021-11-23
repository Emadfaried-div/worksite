from django.urls import path
from django.conf.urls.static import static
from . import views

 

urlpatterns = [
    
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('', views.home,name='home'),
    path('orders/',views.orders,name='orders'),
    path('one_order/<int:id>', views.one_order,name='oneorder'),
    path('about', views.about,name='about'),
    path('po/',views.po,name='po'),
    path('po_details/<int:id>',views.po_details,name='onepo'),
    path('report_create',views.report_create,name='report_create'),
    path('monthly_report',views.monthly_report,name='monthly_report'),
    path('one_report/<int:id>',views.one_report,name='one_report'),
    path('createnote',views.dailynotescreate,name='createnote'),
    path('daily_notes',views.daily_notes,name='daily_notes'),
    path('offer',views.offer, name='offer'),
    path('oneoffer/<int:id>',views.oneoffer,name='oneoffer'),
    path('monthtasks',views.list_view,name='monthtasks'),
    path("search/",views.SearchView.as_view(),name="search"),
    path('delete/<int:id>',views.delete_view,name='delete'),
    path('update/<int:id>',views.update_view,name='update'),
    path('month_task_create',views.monthtasksform,name='month_task_create'),
    
]
