# Import necessary libraries
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape data from Vikaspedia
def fetch_crop_prices():
    url = "https://vikaspedia.in/agriculture/market-information/minimum-support-price"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Scrape and parse the table with crop prices
    crop_data = []
    for row in soup.select("table tr")[1:]:  # Skipping header row
        columns = row.find_all("td")
        if columns:
            crop_name = columns[0].get_text(strip=True)
            price = columns[1].get_text(strip=True)
            crop_data.append({"crop": crop_name, "price": price})
    return crop_data

@app.route('/get_crop_price', methods=['GET'])
def get_crop_price():
    crop_name = request.args.get('crop')
    crop_data = fetch_crop_prices()
    for crop in crop_data:
        if crop_name.lower() in crop["crop"].lower():
            return jsonify(crop)
    return jsonify({"error": "Crop not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
