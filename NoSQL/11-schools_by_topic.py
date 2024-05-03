#!/usr/bin/env python3
""" Find topics  """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic."""
    if mongo_collection is None:
        return []

    return mongo_collection.find({"topics": topic})
