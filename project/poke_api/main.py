from utils import clean_descriptions, index_match, save_clean_df_to_csv
import pandas as pd
import os

cwd = os.getcwd()
path_to_raw_df = f'{cwd}/data/poke_df.csv'
path_to_clean_df = f'{cwd}/data/clean_poke_df.csv'

raw_df = pd.read_csv(path_to_raw_df)
clean_df = clean_descriptions(raw_df)
index_results = index_match(raw_df, clean_df)

save_clean_df_to_csv(raw_df,clean_df,index_results,path_to_clean_df)