Technologies and Programming Languages
######################################

The application is built on the following technologies, chosen for their stability, performance, and compatibility within a modern containerized environment.

Core Stack
----------
* **Python (3.12.3):** Primary programming language.
* **Django (4.x):** Main web framework for rapid development and ORM features.
* **SQLite3:** Database backend. Used for simplicity and portability across the development and deployment environments.
* **Gunicorn:** WSGI HTTP Server for serving the Django application in production.
* **WhiteNoise:** Used for serving static files efficiently.

DevOps and Monitoring
---------------------
* **Docker & Docker Compose:** Used for local development (Quick Start) and production containerization.
* **GitHub Actions:** Used for the Continuous Integration/Continuous Deployment (CI/CD) pipeline.
* **Sentry:** Application performance monitoring and real-time error tracking (critical error logging is integrated into application views).

Development Tools
-----------------
* **Flake8:** Used in the CI pipeline for code style and linting (enforcing PEP 8 compliance).
* **Pytest:** Used for running unit and integration tests (ensuring functional integrity).
* **Sphinx & Read the Docs:** Tools used to generate and host this technical documentation.