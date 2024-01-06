import pandas as pd
import os
import re

cwd = os.getcwd()
path_to_raw_df = f'{cwd}/data/poke_df.csv'
path_to_clean_df = f'{cwd}/data/clean_poke_df.csv'

raw_df = pd.read_csv(path_to_raw_df)

# create a dictionary that stores the index and cleaned text
clean_text = {'id': [], 'c_description':[]}
c_description = []
id_list = []

# iterate thorugh the df
subset_df = raw_df[['id','name','description']]

subset_df = subset_df.iloc[:10]                     # extract top 10 rows


for index, row in subset_df.iterrows():
    # replace "POKéMON" with the name of the pokemon for better results.
    raw_text = row['description']
    name = row['name'].upper()
    
    remove_new_line = re.sub('\n',' ', raw_text)
    remove_esc_seq = re.sub('\u000c', ' ', remove_new_line)
    remove_zero_bytes = re.sub('\x0c', ' ', remove_esc_seq)

    substituted_text = remove_zero_bytes.replace("POKéMON",name)
    
    id_list.append(index)
    c_description.append(substituted_text)

clean_text['id'] = id_list
clean_text['c_description'] = c_description

clean_df = pd.DataFrame(data=clean_text)

# run check to ensure n rows are the same between df and dict.keys()




# append new column to df
final_df = pd.merge(raw_df, clean_df['c_description'], left_index=True, right_index=True)
final_df.to_csv(path_to_clean_df, index=False)


# next steps: wrap in functions





