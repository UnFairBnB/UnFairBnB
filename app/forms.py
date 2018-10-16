from django import forms

from .models import Appartment
from django.forms import ModelForm

class ReturnForm(forms.Form):
    your_name = forms.CharField(label='Return', max_length=100)

class AppartmentForm(ModelForm):
    class Meta:
        model = Appartment
        fields = (
          'area', 
          'acommodates', 
          'bathrooms',
          'bedrooms',
          'type',
          'private',
          'wifi',
          'TV',
          'lock',
          )
