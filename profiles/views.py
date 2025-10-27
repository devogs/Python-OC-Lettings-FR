"""
View functions for the 'profiles' application, handling the listing and detail pages for user profiles.
"""
from django.shortcuts import render, get_object_or_404
from .models import Profile


# Renamed: profiles_index -> index
def index(request):
    """
    Renders the index page listing all user profiles.

    Retrieves all Profile objects from the database and passes them to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Context:
        profiles_list (QuerySet): A list of all available Profile objects.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Unchanged: profile
def profile(request, username):
    """
    Renders the detail page for a specific user profile.

    Retrieves a single Profile object based on the linked User's username. 
    Returns a 404 error if the profile or user is not found.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the associated User to retrieve the profile for.

    Context:
        profile (Profile): The retrieved Profile object.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)