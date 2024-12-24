import requests

from app.db.mongo_db.connection import get_collection, get_collection_coordinates


# Fetch coordinates for a city from OpenCage API
def fetch_coordinates(city):
    api_key = "b469e8507e3d452c8ba8a18301221c30"
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            return latitude, longitude
    return None, None


def process_and_store_coordinates():
    events_collection = get_collection()
    coordinates_collection = get_collection_coordinates()

    # Fetch distinct cities from the events collection
    cities = events_collection.distinct("location.city")
    processed_cities = set()  # To track processed cities

    for city in cities:
        if isinstance(city, str) and city.lower() != "unknown" and city not in processed_cities:
            latitude, longitude = fetch_coordinates(city)
            if latitude and longitude:
                # Insert or update the city's coordinates
                coordinates_collection.update_one(
                    {"city": city},
                    {"$set": {"latitude": latitude, "longitude": longitude}},
                    upsert=True
                )
                print(f"Coordinates for {city}: ({latitude}, {longitude}) saved.")
            else:
                print(f"Coordinates for {city} could not be fetched.")

            # Add city to the processed set
            processed_cities.add(city)
        else:
            print(f"Skipping invalid city: {city}")


def checking_if_empty() -> bool:
    return get_collection_coordinates().count_documents({}) == 0
