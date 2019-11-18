from django.urls import path
from alumno import views

urlpatterns = [ 
    
    path('ws/list_users', views.wsListMike, name='wsListMike'),
    path('', views.index, name='index')
]