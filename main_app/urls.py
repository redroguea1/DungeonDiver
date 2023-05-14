from django.urls import path
from . import views 


urlpatterns = [
    #dungeondiver - welcome page
  path('', views.home, name='home'),
  #building view for user's divers/characters
  path('divers/', views.divers_index, name = 'index'),
  path('divers/<int:diver_id>/', views.divers_detail, name = 'detail'),
  path('divers/create/', views.DiverCreate.as_view(), name ='diver_create'),
  path('divers/<int:pk>/update', views.DiverUpdate.as_view(), name ='diver_update'),
  path('divers/<int:pk>/delete', views.DiverDelete.as_view(), name ='diver_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('search/<int:diver_id>', views.search_items, name='search_items')
]
