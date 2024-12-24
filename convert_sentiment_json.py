import pandas as pd

def process_id(df):
    df['_id'] = df['_id'].apply(lambda x: x['$oid'] if isinstance(x, dict) and '$oid' in x else x)
    return df

def split_columns(df):
    def process_sentiment(row):
        if isinstance(row, dict):
            return {
                "comment": row.get("comment", ""),
                "neg": row.get("score", {}).get("neg", 0),
                "neu": row.get("score", {}).get("neu", 0),
                "pos": row.get("score", {}).get("pos", 0),
                "compound": row.get("score", {}).get("compound", 0),
            }
        return {"comment": "", "neg": 0, "neu": 0, "pos": 0, "compound": 0}

    df["sentiment"] = df["sentiment"].fillna({})
    df["sentiment"] = df["sentiment"].apply(lambda x: [process_sentiment(e) for e in x] if isinstance(x, list) else [])
    df = df.explode("sentiment").reset_index(drop=True)
    df["comment"] = df["sentiment"].apply(lambda x: x["comment"] if isinstance(x, dict) else None)
    df["neg"] = df["sentiment"].apply(lambda x: x["neg"] if isinstance(x, dict) else None)
    df["neu"] = df["sentiment"].apply(lambda x: x["neu"] if isinstance(x, dict) else None)
    df["pos"] = df["sentiment"].apply(lambda x: x["pos"] if isinstance(x, dict) else None)
    df["compound"] = df["sentiment"].apply(lambda x: x["compound"] if isinstance(x, dict) else None)
    df = df.drop(columns=["sentiment"])
    return df

def convert_json_to_df(filepath):
    data = pd.read_json(filepath)
    df = pd.DataFrame(data)
    df = process_id(df)
    df = split_columns(df)
    return df
