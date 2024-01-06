import requests
import pandas as pd

def get_poke_description(poke_id: int) -> dict:
    """Fetches data from PokeAPI.

    Args:
        poke_id (int): random integer, max 1017

    Returns:
        dict: json dictionary with pokemon data
    """
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke_id}')
    data = r.json()

    return data

def get_poke_moves(poke_id: int) -> dict:
    """Fetches data from PokeAPI.

    Args:
        poke_id (int): random integer, max 1017

    Returns:
        dict: json dictionary with pokemon data
    """
    r_moves = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}')
    d_moves = r_moves.json()

    return d_moves

def initialize_df() -> pd.DataFrame:
    init_d = {'id': [],
     'name': [],
     'habitat': [],
     'description':[],
     'move': []
    }
    
    return pd.DataFrame(data=init_d)

    
def create_dataset_of_pokemon():
    # begininng parameters
    start_id = 1
    end_id = 10

    df = initialize_df()

    while end_id < 151:
        for i in range(start_id, end_id+1):
            list_of_ids = []
            list_of_names = []
            list_of_habitats = []
            list_of_descriptions = []
            list_of_moves = []
            updated_dict = {}

            poke_id = i
            
            poke_data = get_poke_description(poke_id)
            poke_moves = get_poke_moves(poke_id)

            list_of_ids.append(poke_id)
            list_of_names.append(poke_data['name'])
            list_of_habitats.append(poke_data['habitat']['name'])
            list_of_descriptions.append(poke_data['flavor_text_entries'][6]['flavor_text'])     # Description pulled from Pokemon Sapphire.
            list_of_moves.append(poke_moves['moves'][0]['move']['name'])                        # Grab first pokemon move.
        
            updated_dict = {'id': list_of_ids,
                            'name': list_of_names,
                            'habitat': list_of_habitats,
                            'description': list_of_descriptions,
                            'move': list_of_moves
                            }
        
            # should erase the old values with new
            new_df = pd.DataFrame(data=updated_dict)
            df = pd.concat([df, new_df])

        # new start and end values.
        # will continue to loop until end_id reaches 150.
        start_id = end_id + 1
        end_id += 10
    return df

final_df = create_dataset_of_pokemon()

save_path = '/Users/senna/poke_haiku/project/poke_api/dataframes/poke_df.csv'
final_df.to_csv(save_path, index=False)