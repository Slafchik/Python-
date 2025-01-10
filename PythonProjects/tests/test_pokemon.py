import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '603f2830e712189a078f7034d69af8c2'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '19035'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_check():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Славка'