from django.urls import path
from .views import TaskList

# Put your views here
urlpatterns = [

    path('', TaskList.as_view(), name='tasks'),

]
