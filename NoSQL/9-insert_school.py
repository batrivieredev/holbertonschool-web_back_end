#!/usr/bin/env python3
"""Module for inserting a document in MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key/value pairs for the document to insert

    Returns:
        The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
