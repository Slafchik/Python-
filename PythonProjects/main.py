import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '603f2830e712189a078f7034d69af8c2'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Булька",
    "photo_id": 5
}

body_change = {
    "pokemon_id": "188418",
    "name": "Барабулька",
    "photo_id": 8
}

body_catch = {
    "pokemon_id": "188418"
}

body_knock = {
    "pokemon_id": "188367"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message = response_catch.json()['message']
print(message)

'''response_out = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knock)
print(response_out.text)

message = response_out.json()['message']
print(message)'''