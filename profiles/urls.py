from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    # Renamed from profiles_index to index
    path('', views.index, name='index'), 
    # Unchanged
    path('<str:username>/', views.profile, name='profile'),
]