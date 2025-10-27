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


# Custom Error Handlers
# These variables must be set at the root URLconf level.
handler404 = 'oc_lettings_site.views.custom_404_view'
handler500 = 'oc_lettings_site.views.custom_500_view'