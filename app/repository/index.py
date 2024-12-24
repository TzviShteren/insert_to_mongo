from pymongo import MongoClient, ASCENDING, DESCENDING
from app.db.mongo_db.connection import get_collection


def insert_indexes():
    # Index for filtering attacks by type and region
    get_collection().create_index(
        [("attack_type", ASCENDING), ("location.region", ASCENDING), ("location.country", ASCENDING)])

    # Index for casualties and geolocation mapping
    get_collection().create_index([("casualties.num_killed", DESCENDING), ("casualties.num_wounded", DESCENDING),
                                   ("location.latitude", ASCENDING), ("location.longitude", ASCENDING)])

    # Index for temporal patterns (year, month, day)
    get_collection().create_index([("date.year", ASCENDING), ("date.month", ASCENDING), ("date.day", ASCENDING)])

    # Index for grouping by region and activity
    get_collection().create_index(
        [("group", ASCENDING), ("location.region", ASCENDING), ("location.country", ASCENDING)])

    # Index for correlating targets and attack types
    get_collection().create_index(
        [("target.type", ASCENDING), ("target.subtype", ASCENDING), ("attack_type", ASCENDING)])

    print("Indexes created successfully!")
