from dotenv import load_dotenv
from random import randint
from utils import generate_haiku
import pandas as pd
import logging
import os
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('parameters.log')
        ]
    )

logger=logging.getLogger()
load_dotenv()

# TODO: fix paths
cwd = os.getcwd()
path_to_poke_haiku_df = f'{cwd}/project/haiku_generator/data/poke_haikus.csv'
path_to_clean_df = f'{cwd}/project/poke_api/data/clean_poke_df.csv'
df = pd.read_csv(path_to_poke_haiku_df)
# df = pd.read_csv(path_to_clean_df)
# poke_id = randint(0,149)


# setting k to 20 gives us less random, fun responses. increasing to 60 is more fun.
# setting temp to 90 provides for more fun responses. 80 seems to be the sweet spot.
PERSONAL_TOKEN = os.getenv('COHERE_PERSONAL_TOKEN')
MODEL= os.getenv('CUSTOM_MODEL')
TOKENS=25
TEMPERATURE=0.8
TOP_K=20
RUN_VERSION=2

logger.info(f'Generated haikus using these parameters: tokens={TOKENS}, temperature={TEMPERATURE}, k={TOP_K}')

poke_ids = []
haikus = []

for poke_id in range(0,150):
    haiku = generate_haiku(PERSONAL_TOKEN, MODEL, df, poke_id, TOKENS, TEMPERATURE, TOP_K)
    print(haiku)
    poke_ids.append(poke_id)
    haikus.append(haiku)
    # wait 20 seconds due to rate limit
    time.sleep(20)

saved_haikus = {"poke_id": poke_ids, f"haiku_{RUN_VERSION}": haikus}
haiku_df = pd.DataFrame(data=saved_haikus)
final_df = pd.merge(df, haiku_df[f'haiku_{RUN_VERSION}'], left_index=True, right_index=True)

path_to_haiku_df = f'{cwd}/project/haiku_generator/data/poke_haikus.csv'
final_df.to_csv(path_to_haiku_df, index=False)