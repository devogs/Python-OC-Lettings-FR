from django.contrib import admin
from django.urls import path, include  # <-- IMPORT 'include'

from . import views

urlpatterns = [
    # Main Index View (from oc_lettings_site/views.py)
    path('', views.index, name='index'),

    # Lettings App URLs (using include for modularity)
    path('lettings/', include('lettings.urls')), 

    # Profiles App URLs (using include for modularity)
    path('profiles/', include('profiles.urls')),
    
    # Admin
    path('admin/', admin.site.urls),
]

# Note: The original paths for lettings_index, letting, profiles_index, and profile
# have been REMOVED from this file.