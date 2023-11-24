from django.urls import path
from app2.views import *

app_name='connect2'

urlpatterns = [
    path('page3/',page3,name='page3'),
    path('page4/',page4,name='page4'),
]