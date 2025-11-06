Deployment Procedures and CI/CD Pipeline
########################################

The application employs a robust Continuous Integration/Continuous Deployment (CI/CD) pipeline managed via GitHub Actions to ensure code quality and automated deployment.

CI/CD Pipeline Overview
------------------------

The workflow is structured into three distinct jobs with strict conditional triggers:

Job 1: Lint and Test (CI)
=========================
* **Trigger:** Executes on any push to a feature branch (e.g., ``feat/**``, ``bug/**``, ``refactor/**``, etc.).
* **Process:** Checks out code, installs Python and dependencies (from ``requirements.txt``), runs code style checks (**Flake8**), and executes unit/integration tests (**Pytest**).
* **Purpose:** Ensures code quality and integrity before merging into ``master``.

Job 2: Build and Push Docker Image
==================================
* **Trigger:** Executes **ONLY** after a Pull Request is merged into the ``master`` branch.
* **Process:** Logs into Docker Hub using secrets, builds the production Docker image, and pushes two tags:
    * A unique tag based on the short commit SHA (e.g., ``matt13290/oc-lettings:c2e4f1a9``).
    * The **latest** tag (``matt13290/oc-lettings:latest``).
* **Purpose:** Prepares and versions the application container for deployment.

Job 3: Deploy to Render (CD)
============================
* **Trigger:** Executes **ONLY** after the successful completion of the **Build and Push Docker Image** job, and **ONLY** on a merge to ``master``.
* **Process:** Triggers an external deployment using a secured Render Webhook URL. Render then pulls the newly tagged ``matt13290/oc-lettings:latest`` image and deploys it.
* **Purpose:** Fully automated production deployment.
