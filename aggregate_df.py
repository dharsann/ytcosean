import pandas as pd

df_sentiments = pd.read_csv(r"C:\Users\dhars\PycharmProjects\PythonProject\.venv\sentiments.csv")
df_statistics = pd.read_csv(r"C:\Users\dhars\PycharmProjects\PythonProject\.venv\statistics.csv")
df_details = pd.read_csv(r"C:\Users\dhars\PycharmProjects\PythonProject\.venv\details.csv")

merged_df = pd.merge(df_statistics[["video_id", "viewCount", "likeCount", "dislikeCount"]], df_sentiments[["video_id", "comment", "neg", "neu", "pos", "compound"]], on="video_id", how="inner")
merged_df_2 = pd.merge(merged_df, df_details[["video_id", "title", "duration"]])
merged_df_2.to_csv("senti_stats_details.csv", index=False)