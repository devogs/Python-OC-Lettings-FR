from django.shortcuts import render
# REMOVE: from .models import Letting, Profile
# You can remove this entire line or comment it out:
# from .models import Letting, Profile


def index(request):
    return render(request, 'index.html')


# REMOVE the following functions entirely:
# lettings_index(request)
# letting(request, letting_id)
# profiles_index(request)
# profile(request, username)
