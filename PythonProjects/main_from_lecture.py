import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '603f2830e712189a078f7034d69af8c2'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "skalozub2008@mail.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Булька",
    "photo_id": 5
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

message = response_create.json()['message']
print(message)