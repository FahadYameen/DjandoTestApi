from django.conf.urls import url 
from FactorAApplication import views 

urlpatterns = [ 
    url(r'^api/post', views.posts)
    
]