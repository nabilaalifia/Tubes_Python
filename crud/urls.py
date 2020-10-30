from django.urls import path,include
from crud import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<slug:delname>', views.delete),
]
