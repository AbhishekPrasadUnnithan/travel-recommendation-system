import requests
import pandas as pd
from sqlalchemy import create_engine
import time

from config import (
    GOOGLE_API_KEY,
    GOOGLE_PLACES_API_URL,
    DEFAULT_RADIUS,
    MAX_PAGES,
    DATABASE_URL,
    DEFAULT_CITIES
)

def fetch_all_hotels(city, radius=DEFAULT_RADIUS):
    params = {
        "query": f"hotels in {city}",
        "radius": radius,
        "key": GOOGLE_API_KEY
    }

    hotel_list = []
    page = 1

    while True:
        response = requests.get(GOOGLE_PLACES_API_URL, params=params)
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
        if not next_token or page >= MAX_PAGES:
            break
        params = {
            "pagetoken": next_token,
            "key": GOOGLE_API_KEY
        }
        time.sleep(2)
        page += 1

    return hotel_list

def save_to_db(all_hotels):
    df = pd.DataFrame(all_hotels)
    print("Saving to hotels.db...")
    engine = create_engine(DATABASE_URL)
    df.to_sql("hotels", engine, if_exists="replace", index=False)
    print("Saved successfully!")

if __name__ == "__main__":
    all_hotels = []
    for city in DEFAULT_CITIES:
        print(f"Fetching hotels in {city}...")
        hotels = fetch_all_hotels(city)
        all_hotels.extend(hotels)

    save_to_db(all_hotels)
