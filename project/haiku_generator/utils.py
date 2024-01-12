import cohere
import pandas as pd
import datetime
from random import randint


def generate_haiku(token:str, custom_model:str, df:pd.DataFrame, poke_id:int, tokens, temperature, top_k) -> str:
    prompt_move = df.iloc[poke_id]['move']
    prompt_description = df.iloc[poke_id]['c_description']
    prompt_pokemon = df.iloc[poke_id]['name']
    prompt_habitat = df.iloc[poke_id]['habitat']

    
    llm_prompt = f'Generate a three-line haiku about a Pokemon called: "{prompt_pokemon}". Here is a description of {prompt_pokemon}: {prompt_description}. {prompt_pokemon} can be found in {prompt_habitat}'
    set_max_tokens=tokens
    set_temperature=temperature
    set_k=top_k

    print(f'Haiku Generated for {prompt_pokemon}, poke-id: {poke_id}.')
    
    co = cohere.Client(token)
    response = co.generate(
        model=custom_model,
        prompt=llm_prompt,
        max_tokens=set_max_tokens,
        temperature=set_temperature,
        k=set_k,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    response = 'Prediction:\n{}'.format(response.generations[0].text)
    return response

def create_website_db(path_to_poke_haiku_df: str, save_path_for_final_df: str) -> pd.DataFrame:
    """Create the static db that the website will pull from.

    Args:
        path_to_poke_haiku_df (str): path to compiled haikus
        save_path_for_final_df (str): save path to find the saved df

    Returns:
        pd.DataFrame: final df.
    """
    uuids = []
    dates = []
    poke_ids = []
    haikus = []
    sprites = []

    date = datetime.datetime(2024,1,1).date()
    for i in range(1,366):
        uuid = str(i) + '_' + str(date)
        poke_id = randint(0,149)
        
        uuids.append(uuid)
        dates.append(date)
        poke_ids.append(poke_id)

        date = date + datetime.timedelta(days=1)
         
    poke_haiku_df = pd.read_csv(path_to_poke_haiku_df)
    for id in poke_ids:        
        sprite = poke_haiku_df['sprite_front'].iloc[id]
        raw_haiku = poke_haiku_df['haiku_3'].iloc[id]
        clean_haiku = raw_haiku.lstrip('Prediction: \n')
        
        haikus.append(clean_haiku)
        sprites.append(sprite)

    d = {"uuid": uuids,
        "dates": dates,
        "poke_id": poke_ids,
        "haiku": haikus,
        "sprites": sprites,
    }

    df = pd.DataFrame(data=d)
    df.to_csv(save_path_for_final_df, index=False)
    return df