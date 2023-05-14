from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Diver, Item
import requests
# Create your views here.

#HOME V1
def home(request):
    return render(request, 'home.html')

@login_required
def divers_index(request):
    # HERE need to pass the divers object through to the index HERE 
    divers = Diver.objects.filter(user=request.user)
    return render(request, 'divers/index.html', { 'divers': divers } )

@login_required
def divers_detail(request, diver_id):
    diver = Diver.objects.get(id=diver_id)
    item_form = ItemForm()
    return render(request, 'divers/detail.html', {
      'diver': diver,
      'item_form': item_form
      })

@login_required
class DiverCreate(CreateView):
    model = Diver
    fields = ['name', 'race', 'job', 'backstory', 'level']
    
    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

@login_required
class ItemCreate(CreateView):
   model = Item
   fields = ['name', 'description']

@login_required
def search_items(request, diver_id):
   #retrieving input and diver. 
   userInput = request.POST['name']
   diver = Diver.objects.get(id=diver_id)
   #SEARCH
   response = requests.get(f'https://api.open5e.com/search/?name={userInput}')
   #Parsing of the item to be added to inventory
   results = response.json()
   item = results['results']
   #checking we have returned at least 1 item
   if len(item)>=1:
    #creating an item to pass throw to render to our page.
    charItem = Item()  
    charItem.name = item[0]['name']
    charItem.description = item[0]['text']
    charItem.diver_id = diver_id
    charItem.save()
   else:
    return render(request, 'divers/search.html', {
      'diver': diver,
      'diver_id': diver_id,
    })
   
   return render(request, 'divers/search.html', {
      'diver': diver,
      'item': charItem
   })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      #ADDED THE USER SAVE  
      user.save()
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
