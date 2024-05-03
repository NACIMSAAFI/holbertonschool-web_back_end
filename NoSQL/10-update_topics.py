#!/usr/bin/env python3
""" Changes all topics  """
import pymongo


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school
    document based on the name."""
    if mongo_collection is None:
        return None

    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
