from django.shortcuts import render
from django.views.generic import FormView, ListView
from .models import Project



class IndexView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'
    