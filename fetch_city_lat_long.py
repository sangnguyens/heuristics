#!/usr/bin/env python

"""
This is a command-line tool that figures out the shortest distance to visit all cities in a list.
"""

import geopy
import geopy.distance
import pandas as pd
from random import shuffle
import click

# build a function that takes variable length of strings and returns a list of cities
def my_cities(*args):
    """Build a list of cities from input"""
    return list(args)

def create_cities_dataframe(cities=None):
    """Create a pandas dataframe of cities and their latitudes and longitudes"""
    import geopy.geocoders

    if cities is None:
        cities = [
            "New York",
            "Knoxville",
            "Birmingham",
            "Baltimore",
            "Bangor",
            "Cleveland",
            "Chicago",
            "Denver",
            "Los Angeles",
            "San Francisco",
            "Raleigh",
            "Seattle",
            "Boston",
            "Houston",
            "Dallas",
            "Miami",
            "Atlanta",
            "Fort Worth",
            "Pheonix",
            "San Diego",
        ]

    geolocator = geopy.geocoders.Nominatim(user_agent='tsp_pandas')

    data = [(city, geolocator.geocode(city).latitude, geolocator.geocode(city).longitude) for city in cities]

    df = pd.DataFrame(data, columns=["city", "latitudes", "longitude"])

    return df
