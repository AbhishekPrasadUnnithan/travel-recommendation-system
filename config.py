import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Search Settings
DEFAULT_RADIUS = 5000  # in meters
MAX_PAGES = 3

# Database
DATABASE_URL = "sqlite:///hotels.db"

# Supported Cities (optional)
DEFAULT_CITIES = [
    "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad",
    "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Amritsar", "Coimbatore",
    "Madurai", "Jamshedpur", "Kochi", "Trivandrum", "Mangalore", "Guwahati", "Chandigarh"
]
