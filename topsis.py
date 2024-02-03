import pandas as pd
from textblob import TextBlob
import numpy as np

original_data = pd.read_csv("F:\Data Science\Topsis\Assignment 2\data.csv")


# Function to perform sentiment analysis using TextBlob
def get_sentiment_score(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Apply sentiment analysis to the 'Question' and 'Answer' columns
original_data['Question_Sentiment'] = original_data['question'].apply(get_sentiment_score)
original_data['Answer_Sentiment'] = original_data['answer'].apply(get_sentiment_score)

new_data = original_data[['Question_Sentiment', 'Answer_Sentiment']]

weights = [1, 1]  # Adjust based on your criteria, assuming equal weight for question and answer sentiment
is_benefit = [True, True]  # Assuming higher sentiment scores are considered better

def topsis(dataset, weights=None, is_benefit=None):
    if weights is None:
        weights = [1] * dataset.shape[1]
    else:
        weights = np.array(weights)

    if is_benefit is None:
        is_benefit = [True] * dataset.shape[1]
    else:
        is_benefit = np.array(is_benefit)

    norm_dataset = dataset / np.sqrt(np.sum(dataset ** 2, axis=0))

    weighted_dataset = norm_dataset * weights

    ideal_solution = np.where(is_benefit, np.max(weighted_dataset, axis=0), np.min(weighted_dataset, axis=0))
    negative_ideal_solution = np.where(is_benefit, np.min(weighted_dataset, axis=0), np.max(weighted_dataset, axis=0))

    d_pos = np.sqrt(np.sum((weighted_dataset - ideal_solution) ** 2, axis=1))
    d_neg = np.sqrt(np.sum((weighted_dataset - negative_ideal_solution) ** 2, axis=1))

    performance_score = d_neg / (d_pos + d_neg)

    rankings = np.argsort(performance_score)

    return rankings

rankings = topsis(new_data, weights, is_benefit)
print("Model Rankings:", rankings)

# Save the updated dataset
original_data.to_csv("result.csv", index=False)
