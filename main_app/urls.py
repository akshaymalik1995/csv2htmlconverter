
from django.urls import path 
from .views import home, upload, analysis, delete
urlpatterns = [
    
    path("" , home, name='home'),
    path("upload" , upload , name='upload'),
    path("delete/<int:pk>" , delete , name='delete'),
    path("analysis/<int:pk>" , analysis , name='analysis'),
]