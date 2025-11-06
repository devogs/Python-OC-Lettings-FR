Installation Instructions
#########################

To set up the project locally for development, you require the following tools and should follow these steps.

Prerequisites
-------------

* Git
* Python (3.12+)
* Docker and Docker Compose (recommended for easy environment setup)
* (Optional) Virtual Environment tool (e.g., ``venv``)

Setup with Docker (Recommended)
-------------------------------

This method uses the predefined ``Dockerfile`` and ``docker-compose.yml`` for a one-step setup.

1.  **Clone the Repository:**
    .. code-block:: bash

        git clone <YOUR_REPOSITORY_URL>
        cd Devogs-OC-lettings-FR

2.  **Build and Run Containers:**
    The ``docker-compose.yml`` script simplifies the process.

    .. code-block:: bash

        sudo docker-compose up -d

    This command performs: pull the image, bind the volumes to SQLite3 database, and starting the Django server on port 8000.

3.  **Access Application:**
    The application will be available at ``http://localhost:8000``.

Manual Setup (Python/Venv)
--------------------------

1.  **Install Dependencies:**
    .. code-block:: bash

        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

2.  **Run Migrations:**
    .. code-block:: bash

        python manage.py migrate

3.  **Start Server:**
    .. code-block:: bash

        python manage.py runserver