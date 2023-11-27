from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Item

# Create your views here.

class Home(ListView):
    model = Item
    template_name = 'shop/home.html'
    context_object_name = 'items'

