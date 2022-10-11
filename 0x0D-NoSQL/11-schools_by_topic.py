#!/usr/bin/env python3
"""MongoDB Find"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns 
    the list of school having a specific topic
    """
    return [i for i in mongo_collection.find({"topics": topic})]
