def recommend_products(products, budget):
    # Filter products within budget
    filtered_products = [p for p in products if p['price'] <= float(budget)]
    
    # Sort by review score and price
    sorted_products = sorted(filtered_products, key=lambda x: (-x['review_score'], x['price']))
    
    # Return top 3 recommendations
    return sorted_products[:3]
