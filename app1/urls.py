from django.urls import path
from app1.views import *

app_name='connect1'

urlpatterns = [
    path('mdb5/',mdb5, name='mdb5'),
]
