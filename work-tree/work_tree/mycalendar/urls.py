from django.urls import path
from django.conf.urls.static import static

from . import views

app_name= "mycalendar"
urlpatterns = [
    path('calendarhome/',views.calendarview,name='calendarhome'),
]