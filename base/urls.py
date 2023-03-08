from django.urls import path
from . import views

# Put your views here
urlpatterns = [

    path('', views.tasklist, name='tasks'),

]
