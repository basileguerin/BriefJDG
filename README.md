## Contexte du projet

Le joueur du Grenier, célèbre Youtubeur français a besoin de vous pour son prochain épisode spécial : "Papy grenier : Attrape les tous !".

Son équipe a déjà une développeuse front-end mais elle ne se sent pas très à l'aise avec le back-end et le NoSQL.

Ainsi, vous devrez, à partir de l'API suivante " https://pokebuildapi.fr/api/v1 ", récupérer la liste de tous les pokemon puis la stocker dans une nouvelle collection "pokemon" de votre base de données que vous nommerez "JDG".

​

Ensuite, vous y ajouterez un 899ème Pokemon :

{ "id": 899, "pokedexId": 899, "name": "Darty Papa", "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }

}

​

Enfin vous allez créer deux queries pour faire un update et un delete sur Darty Papa.

​

NB : Peuplerez votre collection via un script python "app.py", vous noterez vos queries d'update et delete dans un fichier "queries.txt" et enfin vous exporterez votre base de données dans un fichier database.json en suivant le tuto suivant (ou un autre ) https://www.geeksforgeeks.org/export-data-from-mongodb/

​

Le JDG vous remercie...

​