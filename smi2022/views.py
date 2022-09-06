from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from smi2022.models import *

class GurnalSmi(ListView):
    model = GurnalSmi

