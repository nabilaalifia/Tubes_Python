from django.urls import path 
from member import views
urlpatterns = [
path('', views.index, name='index'),
]