from django.urls import path

from . import views

app_name = 'lettings'
urlpatterns = [
    # Renamed from lettings_index to index
    path('', views.index, name='index'), 
    # Unchanged
    path('<int:letting_id>/', views.letting, name='letting'),
]