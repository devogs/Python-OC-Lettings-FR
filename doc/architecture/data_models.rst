Database Structure and Data Models
##################################

This section documents the models used to structure the application's data layer, generated automatically from Python docstrings.

Lettings Application Models
---------------------------

The ``lettings`` app manages property listings.

.. automodule:: lettings.models
   :members:

.. autoclass:: lettings.models.Address
   :members:
   :show-inheritance:

.. autoclass:: lettings.models.Letting
   :members:
   :show-inheritance:

Profiles Application Models
---------------------------

The ``profiles`` app manages user-specific data, linked to the default Django User model.

.. automodule:: profiles.models
   :members:

.. autoclass:: profiles.models.Profile
   :members:
   :show-inheritance: