from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
  return HttpResponse('<h1><marquee>This is a http string response.</marquee></h1>')

def page2(request):
  d={
    'string1':'This page is for jinja printing tag.',
    'a':100,
    'b':300,
    'string2':'This is for looping jinja operational tag.',
    }
  return render(request,'page2.html',context=d)