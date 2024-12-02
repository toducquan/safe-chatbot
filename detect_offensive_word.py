from textblob import TextBlob


def detect_offensive_word(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity < 0
