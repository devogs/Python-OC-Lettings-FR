from django.shortcuts import render
# REMOVE: from .models import Letting, Profile
# You can remove this entire line or comment it out:
# from .models import Letting, Profile


def index(request):
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """
    Renders the custom 404 (Page Not Found) error page.
    Note: The exception argument is required by Django for the handler404 function signature.
    """
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Renders the custom 500 (Server Error) error page.
    Note: The 500 handler is always called without the exception argument.
    """
    return render(request, '500.html', status=500)

# REMOVE the following functions entirely:
# lettings_index(request)
# letting(request, letting_id)
# profiles_index(request)
# profile(request, username)


# oc_lettings_site/views.py (Temporary modification)
# def index(request):
#     # Intentional error to force a 500 status
#     raise Exception("Intentional Server Crash for 500 Test") 
#     return render(request, 'index.html')
