import pytest
from google_places_api import fetch_all_hotels

def test_fetch_all_hotels_returns_list():
    hotels = fetch_all_hotels("Delhi", radius=1000)
    assert isinstance(hotels, list)
    if hotels:
        assert "Name" in hotels[0]
        assert "Rating" in hotels[0]
        assert "Address" in hotels[0]
        assert "City" in hotels[0]
        assert "Map Link" in hotels[0]
