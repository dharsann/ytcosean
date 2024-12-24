import pandas as pd

def process_id(df):
    df['_id'] = df['_id'].apply(lambda x: x['$oid'] if isinstance(x, dict) and '$oid' in x else x)
    return df

def convert_json_to_df(filepath):
    data = pd.read_json(filepath)
    df = pd.DataFrame(data)
    df = process_id(df)
    return df
