import requests
import pandas as pd
from sqlalchemy import create_engine
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Fetch hotels from Google Places API
def fetch_all_hotels(city, radius=5000):  # 5 km radius
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"hotels in {city}",
        "radius": radius,
        "key": API_KEY
    }

    hotel_list = []
    page = 1

    while True:
        response = requests.get(base_url, params=params)
        data = response.json()
        results = data.get("results", [])

        for hotel in results:
            name = hotel.get("name")
            rating = hotel.get("rating", 0.0)
            address = hotel.get("formatted_address")
            place_id = hotel.get("place_id")
            google_maps_link = f"https://www.google.com/maps/place/?q=place_id:{place_id}"

            hotel_list.append({
                "Name": name,
                "Rating": rating,
                "Address": address,
                "City": city,
                "Map Link": google_maps_link
            })

        next_token = data.get("next_page_token")
        if not next_token or page >= 3:
            break
        params = {
            "pagetoken": next_token,
            "key": API_KEY
        }
        time.sleep(2)
        page += 1

    return hotel_list

# Save to SQLite DB
def save_to_db(all_hotels):
    df = pd.DataFrame(all_hotels)
    print("Saving to hotels.db...")
    engine = create_engine("sqlite:///hotels.db")
    df.to_sql("hotels", engine, if_exists="replace", index=False)
    print("Saved successfully!")

# Main execution
if __name__ == "__main__":
    cities = [
        "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad",
        "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
        "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ludhiana", "Agra", "Nashik",
        "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Amritsar", "Coimbatore",
        "Madurai", "Jamshedpur", "Kochi", "Trivandrum", "Mangalore", "Guwahati", "Chandigarh"
    ]

    all_hotels = []
    for city in cities:
        print(f"Fetching hotels in {city}...")
        hotels = fetch_all_hotels(city)
        all_hotels.extend(hotels)

    save_to_db(all_hotels)
