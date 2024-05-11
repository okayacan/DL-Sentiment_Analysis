
from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze the sentiment of the given text."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    text = input("Enter a text: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()