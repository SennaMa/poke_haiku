import os
from utils import create_website_db


# TODO: fix paths
cwd = os.getcwd()
path_to_poke_haiku_df = f'{cwd}/project/haiku_generator/data/poke_haikus.csv'
save_path_for_final_df = f'{cwd}/project/website/data/static_dataset.csv'
save_path_for_final_df_json = f'{cwd}/project/website/data/json_static_dataset.json'

create_website_db(path_to_poke_haiku_df, save_path_for_final_df, save_path_for_final_df_json)