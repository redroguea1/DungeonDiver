from django.urls import path
from . import views


urlpatterns = [
    #dungeondiver - welcome page
  path('', views.home, name='home'),
  #building view for user's divers/characters
  path('divers/', views.divers_index, name = 'index'),
    # CBV version
    #path('divers/', views.Divers.as_view(), name='index')
  path('accounts/signup/', views.signup, name='signup')  
]
