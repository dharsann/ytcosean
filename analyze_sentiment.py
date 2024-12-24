from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from get_comments import get_video_comments

def analyze_video_sentiment(comments):
    sentiments = []
    analyzer = SentimentIntensityAnalyzer()
    for comment in comments:
        score = analyzer.polarity_scores(comment)
        sentiments.append({'comment': comment, 'score': score})
    return sentiments

