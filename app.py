import requests
from pymongo import MongoClient
import json

#Récupération de la liste de pokemon grâce à l'API
reponse = requests.get('https://pokebuildapi.fr/api/v1/pokemon')
pokemon_list = reponse.json()

#Connection a la database Mongo
client = MongoClient('localhost', 27018, username='root', password='1234')
db = client['JDG']
collection = db['pokemon']

#Insertion des pokemons
collection.insert_many(pokemon_list)

#Initialisation dunouveau pokémon
new_pkmn = {
    "id": 899,
    "pokedexId": 899,
    "name": "Darty Papa",
    "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923",
    "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows",
    "slug": "Darty Papa",
    "stats": { 
        "HP": 100000000, 
        "attack": 100000000, 
        "defense": 2, 
        "special\_attack": 100000000, 
        "special\_defense": 2, 
        "speed": 1 }
    }

#Insertion de ce nouveau pokemon
collection.insert_one(new_pkmn)

#Export de la database en json
data = []
for document in collection.find():
    data.append(document)

with open('BriefJDG/database.json', 'w') as outfile :
    json.dump(data, outfile, default=str)