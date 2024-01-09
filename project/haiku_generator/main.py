from dotenv import load_dotenv
from random import randint
from utils import generate_haiku
import pandas as pd
import logging
import os


logging.basicConfig(filename="parameters.log", 
					format='%(asctime)s %(message)s')


logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
load_dotenv()
PERSONAL_TOKEN = os.getenv('COHERE_PERSONAL_TOKEN')
MODEL= os.getenv('CUSTOM_MODEL')


# TODO: fix paths
cwd = os.getcwd()
path_to_clean_df = f'{cwd}/project/poke_api/data/clean_poke_df.csv'
df = pd.read_csv(path_to_clean_df)
poke_id = randint(0,149)

# setting k to 20 gives us less random, fun responses. increasing to 60 is more fun.
# setting temp to 90 provides for more fun responses. 80 seems to be the sweet spot.
TOKENS=25
TEMPERATURE=0.8
TOP_K=20

logger.info(f'Generated haiku was creating using these parameters: tokens={TOKENS}, temperature={TEMPERATURE}, k={TOP_K}')
haiku = generate_haiku(PERSONAL_TOKEN, MODEL, df, poke_id, TOKENS, TEMPERATURE, TOP_K)
print(haiku)
