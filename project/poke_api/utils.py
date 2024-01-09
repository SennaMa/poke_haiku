import pandas as pd
import re


def clean_descriptions(raw_df:pd.DataFrame) -> pd.DataFrame:
    """Clean raw text by (1) removing new lines markers,
    esc sequences, and zero bytes, and (2) replacing the term
    "POKéMON" with the pokemon's name for better haikus.

    Args:
        raw_df (pd.DataFrame): raw df with poke-descriptions.

    Returns:
        pd.DataFrame: clean dataframe.
    """
    # initialize dict that stores the index and clean text
    clean_text = {'id': [], 'c_description':[]}
    c_description = []
    id_list = []

    subset_df = raw_df[['id','name','description']]
    # subset_df = subset_df.iloc[:10]                                   # test: extract top 10 rows

    for index, row in subset_df.iterrows():
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
    return clean_df


def index_match(raw_df:pd.DataFrame, clean_df:pd.DataFrame) -> bool:
    """Check that the number of rows are the same between both dataframes.
    The only change should be the text in poke_description.

    Args:
        raw_df (pd.DataFrame): original df.
        clean_df (pd.DataFrame): df with clean poke descriptions.

    Returns:
        bool: index match is true or false
    """
    if raw_df.index.stop != clean_df.index.stop:
        return False
    return True


def save_clean_df_to_csv(raw_df: pd.DataFrame, clean_df: pd.DataFrame, index_check: bool, save_path: str):
    if not index_check:
        raise Exception("Index doesn't match when comparing the raw and clean df. Please review.")
    else:
        # append new column to df
        final_df = pd.merge(raw_df, clean_df['c_description'], left_index=True, right_index=True)
        final_df.to_csv(save_path, index=False)
        print(f'CSV saved to {save_path}.')
