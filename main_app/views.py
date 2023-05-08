from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Diver
# Create your views here.

#HOME V1
def home(request):
    return render(request, 'home.html')
#HOME V2 - CBV

#needs require login
def divers_index(request):
    # HERE need to pass the divers object through to the index HERE 
    divers = Diver.objects.all()
    return render(request, 'divers/index.html', { 'divers': divers } )
#needs require login
def divers_detail(request, diver_id):
   diver = Diver.objects.get(id=diver_id)
   item_form = ItemForm()
   return render(request, 'divers/detail.html', {
      'diver': diver,
      'item_form': item_form
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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#need to require login
class DiverCreate(CreateView):
    model = Diver
    fields = ['name', 'race', 'job', 'backstory', 'level']
