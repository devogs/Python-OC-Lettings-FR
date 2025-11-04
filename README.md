
## Résumé

  

Site web d'Orange County Lettings

  

## Développement local

  

### Prérequis

  

- Compte GitHub avec accès en lecture à ce repository

- Git CLI

- SQLite3 CLI

- Interpréteur Python, version 3.6 ou supérieure

  

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

  

### macOS / Linux

  

#### Cloner le repository

  

-  `cd /path/to/put/project/in`

-  `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

  

#### Créer l'environnement virtuel

  

-  `cd /path/to/Python-OC-Lettings-FR`

-  `python -m venv venv`

-  `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)

- Activer l'environnement `source venv/bin/activate`

- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel

`which python`

- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`

- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`

- Pour désactiver l'environnement, `deactivate`

###  Create a .env
```plaintext
SENTRY_DSN=<your-sentry-dsn>
SECRET_KEY=<your-django-secret-key>
SENTRY_LOG_LEVEL= INFO # Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
SENTRY_EVENT_LEVEL= ERROR # Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL

DJANGO_DEBUG=False
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
```

#### Exécuter le site

  

-  `cd /path/to/Python-OC-Lettings-FR`

-  `source venv/bin/activate`

-  `pip install --requirement requirements.txt`

-  `python manage.py runserver`

- Aller sur `http://localhost:8000` dans un navigateur.

- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

  

#### Linting

  

-  `cd /path/to/Python-OC-Lettings-FR`

-  `source venv/bin/activate`

-  `flake8`

  

#### Tests unitaires

  

-  `cd /path/to/Python-OC-Lettings-FR`

-  `source venv/bin/activate`

-  `pytest`

  

#### Base de données

  

-  `cd /path/to/Python-OC-Lettings-FR`

- Ouvrir une session shell `sqlite3`

- Se connecter à la base de données `.open oc-lettings-site.sqlite3`

- Afficher les tables dans la base de données `.tables`

- Afficher les colonnes dans le tableau des profils, `PRAGMA table_info(oc_lettings_site_profile);`

- Lancer une requête sur la table des profils, `select user_id, favorite_city from

SELECT user_id, favorite_city FROM oc_lettings_site_profile WHERE favorite_city LIKE 'B%';`

-  `.quit` pour quitter

  

#### Panel d'administration

  

- Aller sur `http://localhost:8000/admin`

- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

  

### Windows

  

Utilisation de PowerShell, comme ci-dessus sauf :

  

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`

- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

Le déploiement en production est géré par une chaîne d'intégration et de livraison continues (CI/CD) implémentée via **GitHub Actions**.

### Récapitulatif Haut Niveau

1.  **Workflow Déclencheur :** Toute modification poussée sur la branche `master` déclenche le pipeline.
    
2.  **Compilation & Tests :** Un premier _job_ exécute le linting (`flake8`) et la suite de tests (`pytest`), en s'assurant que la couverture de test est supérieure à 80%.
    
3.  **Conteneurisation (si tests réussis) :** Si les tests passent, un second _job_ utilise le `Dockerfile` pour construire l'image Docker du site, puis la tague avec la version `v1.0.0` et la pousse vers le registre **Docker Hub** (`matt13290/oc-lettings:c8b43dba`).
    
4.  **Déploiement (si conteneurisation réussie) :** Le dernier _job_ effectue le déploiement sur l'hébergeur cloud Render en tirant l'image depuis Docker Hub.

### Configuration Requise

Pour que le pipeline CI/CD fonctionne correctement et que l'application soit sécurisée et surveillée, les variables d'environnement suivantes doivent être configurées:
```plaintext
-   **`SECRET_KEY`**
Local (`.env`) = OUI
GitHub Secret = OUI
Render Variable = OUI
Clé secrète Django pour la sécurité.
        
-   **`ALLOWED_HOSTS`**
Local (`.env`) = OUI
GitHub Secret = OUI
Render Variable = OUI
Liste séparée par des virgules des noms de domaine autorisés (ex: `mon-site.com,www.mon-site.com`).
        
-   **`SENTRY_DSN`**
Local (`.env`) = OUI
GitHub Secret = OUI
Render Variable = OUI
Data Source Name de Sentry pour le suivi des erreurs.
        
-   **`DOCKER_USERNAME`**
Local (`.env`) = NON
GitHub Secret = OUI
Render Variable = NON
Nom d'utilisateur Docker Hub (pour le _login_ dans l'Action).
        
-   **`DOCKER_PASSWORD`**
Local (`.env`) = NON
GitHub Secret = OUI
Render Variable = NON
Jeton d'accès personnel (PAT) de Docker Hub (pour le _login_ dans l'Action).
        
-   **`DATABASE_URL`**
Local (`.env`) = NON (Utilise SQLite3)
GitHub Secret = NON
Render Variable = OUI
URL de connexion à la base de données PostgreSQL de Render.
        
**`DEBUG`**
Local (`.env`) = OUI (Généralement à `True` en local)
GitHub Secret = NON
Render Variable = OUI (Doit être défini à `False` en production).
        
**`PORT`**
Local (`.env`) = NON (Utilise 8000 par défaut)
GitHub Secret = NON
Render Variable = OUI
Port sur lequel le serveur doit écouter (généralement fourni par Render).
```
**Note sur Sentry :** Le système de logs est configuré pour envoyer les événements de niveau `WARNING` et supérieurs à Sentry.

### Étapes de Déploiement (pour le Successeur)

Les étapes suivantes sont nécessaires pour initialiser l'environnement et/ou pousser une version locale. Pour le déploiement continu, il suffit de pousser le ou les commits sur une des branches:
- 'feat/**'
- 'bug/**'
- 'chore/**'
- 'refactor/**'
- 'hotfix/**'

#### 1. Configuration des Secrets GitHub

Assurez-vous que les 4 secrets (`SECRET_KEY`, `ALLOWED_HOSTS`, `SENTRY_DSN`, `DOCKER_USERNAME`, `DOCKER_PASSWORD`) sont correctement définis dans les **Settings > Secrets and variables > Actions** du repository.

#### 2. Démarrage Local via Docker (Pour vérification)

Pour vérifier que l'image construite par le CI/CD est fonctionnelle localement avant le déploiement en production :

1.  **Récupérer l'image depuis Docker Hub (optionnel) :**
    
    ```
    docker pull matt13290/oc-lettings:latest
    ```
    
2.  **Créer un fichier `.env` :** Créez un fichier `.env` à la racine contenant les variables `SECRET_KEY`, `ALLOWED_HOSTS`, et `SENTRY_DSN` pour l'exécution locale.
    
3.  **Lancer le conteneur :** Utiliser `docker-compose` pour démarrer le service web. Le `docker-compose.yml` s'occupe de la migration de la base de données (`sqlite3`) et du lancement du serveur `gunicorn`.
    
    ```
    docker-compose up -d
    ```
    
4.  **Accès :** Le site sera accessible à l'adresse `http://localhost:8000`.
    

#### 3. Déploiement en Production (Flux Standard)

La mise en production est entièrement automatisée par GitHub Actions :

1.  Assurez-vous que le code est bien sur une des branches annexes.

2. L'action GitHub se lancera automatiquement en effectuant les phases de test flake8 et pytest (le test echoue si la couverture est inferieur a 80%)
    
3.  Mergez vos commits finaux sur la branche de déploiement :
    
    ```
    git checkout master 
    git pull origin master 
    git merge feat/implementation 
    git push origin master
    ```
    
4.  L'action GitHub se lancera automatiquement, construira l'image, la poussera sur Docker Hub, puis déclenchera la procédure de déploiement sur la plateforme choisie.
