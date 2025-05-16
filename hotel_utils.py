def filter_hotels(hotels, rating_threshold=None, city=None, hotel_name_query=None):
    """
    Filter hotels based on rating, city, and optional hotel name query.
    
    Args:
        hotels (list of dict): List of hotels (each as a dictionary).
        rating_threshold (float, optional): Minimum rating.
        city (str, optional): City name to filter by.
        hotel_name_query (str, optional): Keyword to search in hotel names.

    Returns:
        list of dict: Filtered hotel list.
    """
    filtered = hotels

    if rating_threshold is not None:
        filtered = [hotel for hotel in filtered if hotel.get("Rating", 0) >= rating_threshold]

    if city:
        filtered = [hotel for hotel in filtered if hotel.get("City", "").lower() == city.lower()]

    if hotel_name_query:
        filtered = [hotel for hotel in filtered if hotel_name_query.lower() in hotel.get("Name", "").lower()]

    return filtered
