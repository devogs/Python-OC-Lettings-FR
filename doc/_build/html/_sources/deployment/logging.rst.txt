Logging and Error Management
###############################

The application utilizes Sentry for real-time error tracking and performance logging, ensuring high availability and proactive bug fixing.

Sentry Configuration
--------------------

Sentry is integrated via the ``settings.py`` file in the main project configuration.

1.  **DSN (Data Source Name):** The Sentry DSN is stored as an environment variable in the production environment.
    * **Variable Name:** ``SENTRY_DSN``
    * **Value:** The unique URL provided by Sentry.
    
    If ``SENTRY_DSN`` is missing, Sentry initialization is automatically skipped, preventing application failure in development environments.

2.  **Usage of Sentry:**
    All unhandled exceptions (500 errors) in Django are automatically captured by Sentry. Developers should monitor the Sentry dashboard for:
    * New errors and regressions.
    * Performance issues (N+1 queries, slow view rendering).
    