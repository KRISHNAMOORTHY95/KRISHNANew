queries = {
    "providers_per_city": """
        SELECT city, COUNT(*) AS total_providers 
        FROM providers 
        GROUP BY city
    """,
    "most_contributing_type": """
        SELECT type, COUNT(*) AS contributions 
        FROM providers 
        JOIN food_listings ON providers.Provider_ID = food_listings.Provider_ID 
        GROUP BY type
        ORDER BY contributions DESC
    """
}
