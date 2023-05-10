from django.urls import path
from . import views


urlpatterns = [
    #dungeondiver - welcome page
  path('', views.home, name='home'),
  #building view for user's divers/characters
  path('divers/', views.divers_index, name = 'index'),
  path('divers/<int:diver_id>/', views.divers_detail, name = 'detail'),
  path('divers/create/', views.DiverCreate.as_view(), name ='diver_create'),
    # CBV version
    #path('divers/', views.Divers.as_view(), name='index')
  path('accounts/signup/', views.signup, name='signup'),
  path('divers/search/', views.search_items, name='search_items')
]
