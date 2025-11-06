Usage Guide and Use Cases
#########################

This section describes the application's functionality from an end-user and administrator perspective.

Application Architecture Overview
---------------------------------

The application's logic is cleanly separated into two distinct Django applications (modules):

* **Lettings:** Manages the property listings (data retrieval and display, using ``Address`` and ``Letting`` models).
* **Profiles:** Manages user data and associated profiles (data retrieval and display, using the ``Profile`` model linked to the default Django ``User``).

All core data retrieval functionalities are designed with robust error handling, utilizing a try/except block that logs critical database failures internally to Sentry before triggering a custom 500 error page.

Core Functionalities (End-User Focus)
-------------------------------------

1.  **Viewing Lettings (List Index):**
    * **URL:** ``/lettings/``
    * **Description:** Renders the main index page, displaying a list of all available property listings retrieved from the database.
    * **Logging:** Records access attempts at **INFO** level and retrieval success at **DEBUG** level.
    * **Use Case:** A new user browsing the site seeks a quick overview of available properties.

2.  **Viewing Letting Details:**
    * **URL:** ``/lettings/<int:letting_id>/``
    * **Description:** Renders the detail page for a specific rental listing, showing its title and associated address information. If the ID is not found, Django's ``get_object_or_404`` returns a 404 error page.
    * **Logging:** Records access attempts at **INFO** level, including the specific ID being queried.

3.  **Viewing Profiles (List Index):**
    * **URL:** ``/profiles/``
    * **Description:** Renders the index page listing all registered user profiles.
    * **Logging:** Records access attempts at **INFO** level.
    * **Use Case:** An administrator verifies the list of currently registered users.

4.  **Viewing Profile Details:**
    * **URL:** ``/profiles/<str:username>/``
    * **Description:** Renders the detail page for a specific user profile, retrieved using the username. If the profile is not found, a 404 error page is displayed.
    * **Logging:** Records access attempts at **INFO** level, including the username being queried.

Error Handling and Monitoring (Administrator Focus)
---------------------------------------------------

The application implements custom error handling for better user experience and robust monitoring.

* **404 (Not Found):** Handled by ``custom_404_view`` (mapped by ``handler404``). Displays the custom ``404.html`` template with an HTTP 404 status.
* **500 (Server Error):** Handled by ``custom_500_view`` (mapped by ``handler500``). This view is automatically triggered when a view function raises an unhandled exception (e.g., a critical database failure).

**Monitoring Procedure:**

1.  **Critical Failure Logging:** When a database exception occurs (e.g., in ``lettings.views.index``), the exception is logged at the **ERROR** level with `exc_info=True`.
2.  **Sentry Capture:** Due to the Sentry integration, this critical **ERROR** log event is immediately captured and reported to the Sentry dashboard.
3.  **Administrator Action:** The administrator should monitor Sentry for exceptions containing the critical log message (e.g., "Critical error retrieving lettings list from DB") to diagnose infrastructure or data issues instantly.

Administration Interface (Django Admin)
---------------------------------------

The Django Administration interface is the primary tool for managing content and user data.

* **URL:** ``/admin/``
* **Access:** Requires a **superuser** account.

**Key Administrative Tasks:**

* **Lettings Management:**
    * Create, modify, or delete **Letting** objects.
    * Create, modify, or delete **Address** objects (linked to Lettings).
* **Profiles Management:**
    * Manage **Profile** objects, which contain the link to the user's account.
* **User & Group Management:**
    * Manage default Django **User** accounts (permissions, passwords).

All custom models are registered in their respective ``admin.py`` files, ensuring the separation of concerns is maintained even in the administrative back-end.