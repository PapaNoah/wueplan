from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView, DetailView
from datetime import datetime
from datetime import timedelta
from .models import Times, Station, Lines
from .forms import BusSelectionForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

def search_form(request):
  return render(request, 'search.html')
    
def search(request):
  print "POST", request.POST
  cont = dict()
  line = request.POST['line']
  station = request.POST['station']
  now = datetime.now()
  times_list = Times.objects.filter(lines__name=line,station__name=station,time__gt=now)
  print times_list
  return render(request, 'search.html', {"line" : line, "times_list" : times_list})
  
class TimeDetailView(DetailView):
  model = Times
  template_name = 'times/detail.html'
  
  def get_context_data(self, **kwargs):
    context = super(TimeDetailView, self).get_context_data(**kwargs)
    return context