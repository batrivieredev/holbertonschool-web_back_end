#!/usr/bin/env python3
"""Module for finding schools by topic"""
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic: (string) topic searched

    Returns:
        List of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
