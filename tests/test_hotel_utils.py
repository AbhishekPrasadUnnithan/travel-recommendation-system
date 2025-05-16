from hotel_utils import filter_hotels

def test_filter_by_rating_and_city():
    hotels = [
        {"Name": "Hotel A", "Rating": 4.5, "City": "Mumbai"},
        {"Name": "Hotel B", "Rating": 3.8, "City": "Delhi"},
        {"Name": "Hotel C", "Rating": 4.2, "City": "Mumbai"},
    ]
    result = filter_hotels(hotels, rating_threshold=4.0, city="Mumbai")
    assert len(result) == 2
    assert all(h["City"] == "Mumbai" and h["Rating"] >= 4.0 for h in result)

def test_filter_hotels_empty_list():
    result = filter_hotels([], rating_threshold=4)
    assert result == []

def test_filter_hotels_no_matching_city():
    hotels = [{"Name": "A", "Rating": 5, "City": "Delhi"}]
    result = filter_hotels(hotels, rating_threshold=4, city="Mumbai")
    assert result == []
