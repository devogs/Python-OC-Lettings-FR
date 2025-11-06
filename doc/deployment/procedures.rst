Deployment and CI/CD Procedures
###############################

The application relies on a robust Continuous Integration/Continuous Deployment (CI/CD) pipeline, defined in the ``oc-lettings - Lint - Test - Build - Push - Deploy`` GitHub Actions workflow.

The pipeline ensures code quality, integrity, and automated deployment, running on specific branch triggers.

---

CI/CD Pipeline Overview
-----------------------

The workflow consists of three distinct jobs, triggered by code pushes and pull request merges.

1. Job 1: Lint and Test (Code Quality Check)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This job verifies code compliance and functional integrity.

* **Triggers:** Pushed commits on any development/maintenance branch:
    * ``feat/**``, ``bug/**``, ``chore/**``, ``refactor/**``, ``hotfix/**``.

* **Steps Performed:**
    1.  Setup Python environment (Python **3.12.3**).
    2.  Install dependencies from ``requirements.txt``.
    3.  Run static analysis using **Flake8** for PEP 8 compliance.
    4.  Execute Unit and Integration Tests using **Pytest**.

2. Job 2: Build and Push Docker Image (Containerization)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This job is responsible for containerizing the application and storing the image.

* **Triggers:** Only runs upon a successful **Pull Request merge into the ``master`` branch**.
* **Dependencies:** None (must succeed independently).
* **Steps Performed:**
    1.  Logs into Docker Hub using secrets (``DOCKERHUB_USERNAME`` and ``DOCKERHUB_TOKEN``).
    2.  Sets two image tags: a short commit SHA tag and a ``latest`` tag.
    3.  Builds the Docker image from the root ``Dockerfile`` and pushes the image to the **`matt13290/oc-lettings`** repository on Docker Hub.

3. Job 3: Deployment (CD)
^^^^^^^^^^^^^^^^^^^^^^^^^

This final job handles the Continuous Deployment to the hosting environment.

* **Triggers:** Only runs upon a successful **Pull Request merge into the ``master`` branch**.
* **Dependencies:** Requires Job 2 (Build and Push) to complete successfully.
* **Action:** Triggers the deployment hook for Render using a ``curl`` command, which instructs Render to pull the latest image from Docker Hub and deploy it.

    .. code-block:: bash
    
        curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK_URL }}
