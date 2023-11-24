from django.urls import path
from app1.views import *

app_name='connect1'

urlpatterns = [
    path('page2/',page2,name='page2'),
]