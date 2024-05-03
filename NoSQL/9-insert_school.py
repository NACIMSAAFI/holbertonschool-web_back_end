#!/usr/bin/env python3
""" Inserts a new document  """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""

    if mongo_collection is None:
        return None

    inserted_id = mongo_collection.insert_one(kwargs).inserted_id
    return inserted_id
