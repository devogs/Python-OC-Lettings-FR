Project Description
###################

.. This section covers the project scope and the core improvements implemented.

Project Overview
----------------

The Orange County Lettings platform facilitates property rental listings. This version (2.0) is the result of a significant refactoring effort aiming to convert the initial monolithic structure into a modular, maintainable, and scalable application architecture (Site Web 2.0).

Key Architectural Improvements:

* **Modularization:** Codebase split into two distinct Django applications: ``lettings`` and ``profiles``.
* **Data Migration:** Successful migration of legacy data using non-SQL Django migrations.
* **CI/CD Pipeline:** Implementation of automated testing, linting (PEP8), containerization, and deployment procedures.
* **Observability:** Integration of Sentry for error tracking and performance monitoring.

Code Structure
--------------

The codebase adheres to the Django app structure, ensuring a clear separation of concerns:

.. code-block:: none

    .
    ├── lettings/      # Handles property listings (Letting, Address models)
    ├── profiles/      # Handles user profiles (Profile model)
    ├── oc_lettings_site/ # Main project configuration, settings, root URLs, WSGI
    └── doc/           # Sphinx documentation files

Each application contains its own models, views, templates, promoting maintainability and scalability.