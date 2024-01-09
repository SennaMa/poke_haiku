from random import randint
from dotenv import load_dotenv
import cohere
import pandas as pd
import os


# TODO: fix paths
cwd = os.getcwd()
path_to_clean_df = f'{cwd}/project/poke_api/data/clean_poke_df.csv'

def generate_haiku(token:str, custom_model:str, df:pd.DataFrame, poke_id:int) -> str:
    prompt_move = df.iloc[poke_id]['move']
    prompt_description = df.iloc[poke_id]['c_description']
    prompt_pokemon = df.iloc[poke_id]['name']
    prompt_habitat = df.iloc[poke_id]['habitat']

    # setting k to 20 gives us less random, fun responses. increasing to 60 is more fun.
    # setting temp to 90 provides for more fun responses. 80 seems to be the sweet spot.
    llm_prompt = f'Generate a three-line haiku that about the Pokemon called "{prompt_pokemon}". Here is a description of {prompt_pokemon}: {prompt_description}. {prompt_pokemon} knows the move {prompt_move} and {prompt_pokemon} lives in {prompt_habitat}.'
    set_max_tokens=25
    set_temperature=0.80
    set_k=20

    print(f'Haiku Generated for {prompt_pokemon}, poke-id: {poke_id}. It knows the move: {prompt_move}')
    
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
