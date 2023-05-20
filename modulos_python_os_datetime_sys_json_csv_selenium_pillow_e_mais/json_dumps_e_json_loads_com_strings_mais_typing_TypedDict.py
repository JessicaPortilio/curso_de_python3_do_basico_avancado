# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

# json.dump  - jogar para fora
# json.load - carregar para dentro

import json
# from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    year: int
    original_title: str
    is_movie: bool
    imdb_rating: float
    characters: list[str]
    budget: None | float


string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

filme: Movie = json.loads(string_json)
# pprint(filme)
# print()
# print(filme['title'])
# print()
# print(filme['year'] + 10)
json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)
