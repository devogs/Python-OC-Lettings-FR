"""
View functions for the 'lettings' application, handling the listing and detail pages for rental properties.
"""
from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Renders the index page for all lettings.

    Retrieves all Letting objects from the database and passes them to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Context:
        lettings_list (QuerySet): A list of all available Letting objects.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting.

    Retrieves a single Letting object based on its ID. Returns a 404 error if not found.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The primary key (ID) of the Letting to retrieve.

    Context:
        title (str): The title of the letting.
        address (Address): The associated Address object for the letting.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)