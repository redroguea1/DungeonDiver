from django.forms import ModelForm, SearchInput
from .models import Item
import requests, forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

    search_term = forms.CharField(widget=SearchInput())

    def clean(self):
        super().clean()

        search_term = self.cleaned_data['search_term']

        # Make an HTTP request to the Open5e API.
        response = requests.get('https://api.open5e.com/search/?text=' + search_term)

        # If the HTTP request is successful, parse the response and populate the form fields with the results.
        if response.status_code == 200:
            results = response.json()
            for result in results:
                self.fields['name'].initial = result['name']
                self.fields['description'].initial = result['description']

        # If the HTTP request is not successful, raise an exception.
        else:
            raise forms.ValidationError('An error occurred while searching the Open5e API.')