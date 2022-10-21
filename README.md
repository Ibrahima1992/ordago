# exercice_ordago
# Backend
# start the environment
    #docker-compose up -d (to start the env)
# go to the api to add a user in the database with the route (webbrowser)
    http://localhost:8000/docs
    with the endpoint POST : /test-ordago/users
    example: {
              "lastname": "string",
              "firstname": "string",
              "login": "string",
              "email": "string",
              "password": "string"
            }
    add a new user
# look for gui
    http://localhost:3000/login
    and try authentificate with
        login: string
        password: string
    if authentification is success you will be redirect to home page
    here you can edit your mail and see the changes.
  
# go to the api with the route /test-ordago/users to see the user to see that his email has changed [in the sense that we add only one user to list ]
