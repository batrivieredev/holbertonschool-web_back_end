#!/usr/bin/env python3
"""Module for listing all documents in MongoDB collection"""
from typing import List


def list_all(mongo_collection) -> List:
    """Lists all documents in a collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents or empty list if no documents
    """
    return list(mongo_collection.find())
