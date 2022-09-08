from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from smi2022.models import *
from django.core.paginator import Paginator

class GurnalSmi(ListView):
    paginate_by = 2
    model = GurnalSmi
    #smi = GurnalSmi.objects.all()
    #p = Paginator(smi, 10)

class GurnalSmiSocNet(ListView):
    model = GurnalSocNet
