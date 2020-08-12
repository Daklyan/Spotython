# Spotython
Usage of Spotify API in python. Process and display of stats form the user data via web interface : tracks, artists, ...

# Configuration of the project
## To configure the project in `pycharm`
- `Preferences -> Languages & Frameworks -> Django`
    - Activate Django support and give the root files of the Django project, settings and script manage
- Add Django plugin to your Python interpreter 
    - `Settings -> Project interpreter -> Add Django`

https://www.it-swarm.dev/fr/python/comment-configurer-le-projet-django-dans-pycharm/1047588497/

## Install dependencies
```BASH
pip install -r requirements.txt
```

## Modify the client ID and client Secret in api_spotify/controller/secret.json

```JSON
{
  "Spotify_Client_ID": "CLIENT_ID",
  "Spotify_Client_Secret": "CLIENT_SECRET"
}
```

## Set the Database
 
- Create a database : `spotython`

- Launch migrations :

        python manage.py migrate


# Start project

To start the project via a terminal:

    python manage.py runserver
