"""
URL: https://pokeapi.co/api/v2/pokemon/35

What's available:
- sprites for visual component
- species > url > generation > flavor_text (https://pokeapi.co/api/v2/pokemon-species/35/)

Species Example: https://pokeapi.co/api/v2/pokemon-species/35/
"""

import requests
import random

def generate_poke_id() -> int:
    """Generate a poke_id, starting from 001: Bulbasaur
    to max poke_id 1017: Ogerpon.

    Returns:
        int: pokemon_id
    """
    return random.randrange(1,1018)

def get_poke_description(poke_id: int) -> dict:
    """Fetches data from PokeAPI.

    Args:
        poke_id (int): random integer, max 1017

    Returns:
        dict: json dictionary with pokemon data
    """
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke_id}')
    data = r.json()

    # print(poke_id)
    # print(data['name'])
    # print(data['base_happiness'])

    return data

poke_id = generate_poke_id()
poke_data = get_poke_description(poke_id)

print(poke_data['name'])
print(poke_data['base_happiness'])