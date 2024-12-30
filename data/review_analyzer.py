from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_reviews(reviews):
    scores = []
    for review in reviews:
        result = sentiment_analyzer(review)
        scores.append(result[0]['score'] if result[0]['label'] == 'POSITIVE' else -result[0]['score'])
    return sum(scores) / len(scores) if scores else 0
