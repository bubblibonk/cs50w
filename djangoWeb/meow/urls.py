from django.urls import path 
from . import views
urlpatterns=[path("",views.index,name="index"),
             path("bonk",views.bonk,name="bonk"),
             path("<str:name>",views.greet,name="greet")
             ]
