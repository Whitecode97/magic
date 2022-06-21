from django.urls import path
from .views import feedback, home

app_name = "home"

urlpatterns = [ 
    
    path("", home, name = "home"),
    path("feedback/", feedback, name = "feed")
    
    ] 