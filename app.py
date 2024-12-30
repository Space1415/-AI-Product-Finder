from flask import Flask, render_template, request, jsonify
from data.product_scraper import scrape_products
from data.review_analyzer import analyze_reviews
from data.recommender import recommend_products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find_products():
    user_query = request.form['query']
    region = request.form['region']
    budget = request.form['budget']
    
    # Step 1: Scrape products
    products = scrape_products(user_query, region)
    
    # Step 2: Analyze reviews
    for product in products:
        product['review_score'] = analyze_reviews(product['reviews'])
    
    # Step 3: Recommend products
    recommendations = recommend_products(products, budget)
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
