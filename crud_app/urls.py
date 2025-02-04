from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
     
     path('',home,name="home"),
     path('form/' ,form , name="form"),
     path('about/',about ,name="about"),
     path('contact/',contact ,name="contact"),
     path('delete/<int:id>',delete_data,name="delete_data"),
     path('clear/',clear,name="clear"),
     path('recycle/',recycle,name="recycle"),
     path("restore/<int:id>",restore,name="restore"),
     path("edit/<int:id>",edit,name="edit")
]
