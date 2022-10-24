<!--
    Pour le teste technique, j'ai décidé de le faire avec la librairie python fastAPI,
    sqlAlchemy comme ORM j'ai embarqué Postgres pour la base de données.

    J'ai decidé de cette technologie, pour profiter suite à l'entretien 
    qu'on avait eu en lien avec le poste pour profiter pour vous faire découvrir 
    la technologie fastAPI qui était aussi très adaptée par rapport à la demande.

                ---- Fonctionnalités ----

    - Importer les données (csv) et le traitement qui lui ai associé ave la librairie pandas
    - Ajouter un utilisateur (login && password) car l'API est authentifiée
        Exemple: login: ordago et password:ordago
    - Exposer l'API (les endpoints)

                ---- Architecture ----

    Architecture micro service dockerisé
    API: fastapi + SqlAlchemy
    BASE_DE_DONNÉES: Postgres
--> 
---------------------------------------------------------
    POUR LANCER LA STACK EN MODE DEVELOPPEMENT

# 1- Cloner le projet
    git clone git@github.com:Ibrahima1992/ordago.git

# 2- Se déplacer dans le répertoire ordago
    cd ordago

# 3- Se servir du Makefile pour lancer la stack
    make start

# 4- Importer les données data (automobile.csv)
    make load_data

# 5- Accès à l'API
    make status

<!--    Pour visualiser l'API (swagger Documentation)   -->
rendez-vous sur le lien: http://localhost:8000/

<!--    Pour acceder à la base de données  --->
    Une fois dans la base de données avec "make bdd" par exemple:
    y'a un utilisateur et mot de passe: "user:ordago" et "password:ordago"

    - psql -h localhost -U ordago ordago
--------------------------------------------------------

####    OPTIONS POUR CONTROLLER LES DOCKERS    ####

# Stop les services (API, BDD)
    make stop

# Rédemarrer les services
    make restart

# Accès API
    make api_auto

# Accès BDD
    make bdd

---------------------------------------------------------