# Spotython
Exploitation de l'API de spotify en python. Utilisation et affichage de statistique des données d'un utilisateur via une interface web : son, artiste, album....

# Configuration du project
## Pour configurer le projet sur `pycharm`
- `Preferences -> Languages & Frameworks -> Django`
    - Activer le support Django et donnez les fichiers racine du projet Django, Paramètres et Gestion du script
- Ajouter le plugin Django dans votre interpréteur python 
    - `Settings -> Project interpreter -> Ajouter Django`

https://www.it-swarm.dev/fr/python/comment-configurer-le-projet-django-dans-pycharm/1047588497/

## Installer les dépendances 
```
pip install -r requirements.txt
```

## Modifier le client ID et le client Secret dans api_spotify/controller/api.py
```python
os.environ['SPOTIPY_CLIENT_ID'] = 'CLIENT ID' # Mettre l'id de l'app
os.environ['SPOTIPY_CLIENT_SECRET'] = 'CLIENT SECRET' # Mettre le secret de l'app
```

## Configurer la BDD
 
- Créer une base de donnée : `spotython`

- Lancer les migrations :

        python manage.py migrate


# Start project

Pour lancer le serveur web depuis le terminal:

    python manage.py runserver