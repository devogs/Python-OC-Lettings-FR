Quick Start Guide
#################

This guide provides the fastest way to get the application running and testing core features.

Launching the Application
-------------------------

Assuming you have cloned the repository and have Docker installed:

1.  Execute the local run script from the project root:
    .. code-block:: bash

        sudo docker compose up -d

2.  Wait for the logs to show "Container python-oc-lettings-fr-web-1  Started".
3.  Open the application's root index: `http://localhost:8000`

Testing Data Integrity
----------------------

To verify that the modularization and data migration were successful, navigate to the listing indices:

* **Lettings Index:** `http://localhost:8000/lettings`
* **Profiles Index:** `http://localhost:8000/profiles`

You should see all original listings and profiles correctly associated via the foreign key relationships.

Running Tests
-------------

To ensure all functionalities and migrations are stable:

1.  Run the Pytest command
    .. code-block:: bash

        pytest
        