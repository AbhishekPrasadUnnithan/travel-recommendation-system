# Hotel Recommendation System

A travel accommodation recommendation system built using **Google Places API**, **Streamlit**, and **SQLite**, designed to help users filter and explore hotels based on **location** and **customer ratings**, with an optional hotel name search.

---

## Features

- Filter hotels by:
  - City
  - Rating range
  - Optional hotel name search
- Google Maps link for each hotel
- Clean and intuitive UI built with Streamlit
- Data stored locally in SQLite using SQLAlchemy
- Uses `config.py` for centralized configuration management

---

## Tech Stack

- Python 3.10+
- Streamlit
- SQLite + SQLAlchemy
- Pandas
- Google Places API
- dotenv for environment variable management
- Pytest for testing

---

## Key Updates & Notes

- **Price level filtering removed** due to unreliable and inconsistent data from Google Places API.
- Radius for hotel search is set to **5 km** to cover a wide area inside cities.
- Added **more cities across India** for a comprehensive dataset.
- Hotels are filtered and recommended **only based on rating** and optional name search.
- Google Maps links are provided for each hotel to view their location and details directly.
- Uses `config.py` to store API keys, base URLs, city list, and DB paths — improving maintainability and scalability.

---

## Limitations & Assumptions

Due to restrictions of the Google Places API:

- Actual hotel price values are **not available** via the API unless the hotel integrates with Google’s booking partners — which is rare.
- Price level information is often missing or inconsistent; hence, the app **does not filter by price** to avoid misleading users.
- This system relies primarily on **hotel ratings** for recommendations.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AbhishekPrasadUnnithan/travel-recommendation-system.git
cd travel-recommendation-system
