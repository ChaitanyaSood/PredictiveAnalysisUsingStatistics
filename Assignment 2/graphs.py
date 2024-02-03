import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import topsis as t

original_data = pd.read_csv("data.csv")
result_data=pd.read_csv("result.csv")


plt.figure(figsize=(12, 6))
plt.bar(range(len(t.new_data.columns)), t.new_data.mean(), align='center', alpha=0.7)
plt.xticks(range(len(t.new_data.columns)), t.new_data.columns)
plt.xlabel('Sentiment Analysis')
plt.ylabel('Average Sentiment Score')
plt.title('Original Dataset Sentiment Analysis')
plt.show()

# Display table with original dataset sentiment scores
original_sentiment_table = t.new_data.describe().transpose()[['mean', 'std']]
original_sentiment_table.columns = ['Mean Sentiment Score', 'Standard Deviation']
print("\nOriginal Dataset Sentiment Analysis Table:")
print(original_sentiment_table)


plt.figure(figsize=(12, 6))
plt.bar(range(len(t.rankings)), t.rankings[t.rankings], align='center', alpha=0.7, label='Result File')
plt.xticks(range(len(t.rankings)), [f"Model {i+1}" for i in t.rankings])
plt.xlabel('Models')
plt.ylabel('Performance Score')
plt.title('TOPSIS Analysis Results')
plt.legend()
plt.show()

# Display table with result file dataset rankings and performance scores
result_results_table = pd.DataFrame({'Model': [f"Model {i+1}" for i in t.rankings], 'Rank': range(1, len(t.rankings)+1), 'Performance Score': t.rankings[t.rankings]})
print("\nResult File Dataset Results Table:")
print(result_results_table)

avg_sentiment_original = t.new_data.mean()
avg_sentiment_result = result_data[['Question_Sentiment', 'Answer_Sentiment']].mean()

# Combine the averages into a single DataFrame
compare_df = pd.DataFrame({'Original Dataset': avg_sentiment_original, 'TOPSIS Result': avg_sentiment_result})

# Plot the bar chart
compare_df.plot(kind='bar', figsize=(12, 6))
plt.title('Comparison of Average Sentiment Scores and TOPSIS Performance Scores')
plt.xlabel('Sentiment Analysis')
plt.ylabel('Average Score')
plt.show()