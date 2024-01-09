from dotenv import load_dotenv
from random import randint
from utils import generate_haiku
import pandas as pd
import os

load_dotenv()
PERSONAL_TOKEN = os.getenv('COHERE_PERSONAL_TOKEN')
MODEL= os.getenv('CUSTOM_MODEL')

# TODO: fix paths
cwd = os.getcwd()
path_to_clean_df = f'{cwd}/project/poke_api/data/clean_poke_df.csv'

# input
df = pd.read_csv(path_to_clean_df)
poke_id = randint(0,149)

s = generate_haiku(PERSONAL_TOKEN, MODEL, df, poke_id)
print(s)
