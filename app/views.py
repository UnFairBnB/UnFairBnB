# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import csv

from .forms import AppartmentForm, ReturnForm
from .models import Appartment
from .resources import AppartmentResource

class HomeView(TemplateView):
    template_name = 'index.html'

class SubmitView(TemplateView):
    template_name = 'submit.html'

class AreaView(CreateView):
    model = Appartment
    form_class = AppartmentForm
    template_name = 'index.html'

def get_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppartmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/submit')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppartmentForm()

    return render(request, 'index.html', {'form': form})

