<!--
    Pour le teste technique, j'ai décidé de le faire avec la librairie python fastAPI,
    sqlAlchemy comme ORM j'ai embarqué Postgres pour la base de données.

    J'ai decidé de ce choix, pour profiter suite à la conversation qu'on avait eu par rapport au poste
    de vous faire découvrir la technologie fastAPI pour exposer l'API.

                ---- Fonctionnalités ----
                
    - Importer les données (csv) et le traitement avec pandas
    - Ajouter un utilisateur (login && password) car l'API est authentifiée
    - Exemple: login: ordago et password:ordago
    - Exposer l'API (les endpoints)

                ---- Architecture ----

    Architecture micro service dockerisé
    API: fastapi + SqlAlchemy
    BASE_DE_DONNÉES: Postgres
--> 

# Pour lancer la stack en mode développement
# Cloner le projet
    git clone git@github.com:Ibrahima1992/ordago.git

# Se déplacer dans le répertoire ordago
    cd ordago

# Se servir du Makefile pour lancer la stack
    make start

# Importer les données data (automobile.csv)
    make load_data

# Stop les services (API, BDD)
    make stop

# Rédemarrer les services
    make restart