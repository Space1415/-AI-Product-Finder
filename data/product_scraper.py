import requests
from bs4 import BeautifulSoup

def scrape_products(query, region):
    url = f"https://example.com/search?q={query}&region={region}"  # Replace with real API or URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    for item in soup.find_all('div', class_='product'):
        products.append({
            'name': item.find('h2').text,
            'price': float(item.find('span', class_='price').text.replace('$', '')),
            'reviews': [review.text for review in item.find_all('p', class_='review')],
        })
    return products
