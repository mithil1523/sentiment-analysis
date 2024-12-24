# project on sentiment analysis 

import matplotlib.pyplot as plt
from textblob import TextBlob
import pandas as pd

# Sample data (a list of texts)
texts = [
    "I love this product! It's amazing.",
    "Horrible experience, I will never buy again.",
    "This is the best purchase I have ever made.",
    "I am not satisfied with the service, it could be better.",
    "Absolutely fantastic, I highly recommend it!",
    "Worst product ever, I hate it.",
    "Good quality, but the delivery was late."
]

# Function to analyze sentiment of each text
def analyze_sentiment(texts):
    sentiments = []
    for text in texts:
        # Create a TextBlob object
        blob = TextBlob(text)
        
        # Sentiment analysis: polarity of the text
        sentiment = blob.sentiment.polarity
        sentiments.append(sentiment)
    
    return sentiments

# Get the sentiment analysis of each text
sentiments = analyze_sentiment(texts)

# Convert the sentiment scores to a DataFrame for easier visualization
df = pd.DataFrame({
    'Text': texts,
    'Sentiment Score': sentiments
})

# Print the DataFrame
print(df)

# Plotting the Sentiment Scores
plt.figure(figsize=(10, 6))
plt.barh(df['Text'], df['Sentiment Score'], color='skyblue')
plt.xlabel('Sentiment Score')
plt.title('Sentiment Analysis of Texts')
plt.show()
