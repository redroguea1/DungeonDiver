from django.forms import ModelForm, forms
from .models import Item
from django.db import models


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name']

