from django.shortcuts import render, HttpResponse
from datetime import datetime


def index(request):
  context = {
  # 'display_time':strftme("%Y-%m-%d %H:%M %p", gmtime())
  "display_time":datetime.now()
  }
  return render(request,'timeDisplay_app/index.html', context)