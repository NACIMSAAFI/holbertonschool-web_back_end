#!/usr/bin/env python3
""" List all documents in Python """
import pymongo


def list_all(mongo_collection):
    """Function that lists all documents in a collection."""

    if mongo_collection is None:
        return []

    return mongo_collection.find()
