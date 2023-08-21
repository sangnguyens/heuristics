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

<<<<<<<<<<<<<  ✨ Codeium AI Suggestion  >>>>>>>>>>>>>>
def create_cities_dataframe(cities=None):
    """Create a pandas dataframe of cities and their latitudes and longitudes"""

+    import pandas as pd
+    import geopy.geocoders
+
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
-        
-    # Create a list to hold the latitudes and logitudes
-    latitudes = []
-    longitudes = []
-
-    # loop through the cities list and get the latitudes and longitudes
-    for city in cities:
-        geolocator = geopy.geocoders.Nominatim(user_agent='tsp_pandas')
-        location = geolocator.geocode(city)
-        latitudes.append(location.latitude)
-        longitudes.append(location.longitude)
-
-    # Create a dataframe from the cities, latitudes and longitude
-    df = pd.DataFrame(
-        {
-            "city": cities,
-            "latitudes": latitudes,
-            "logitude": longitudes,
-        }
-    )
+
+    geolocator = geopy.geocoders.Nominatim(user_agent='tsp_pandas')
+
+    data = [(city, geolocator.geocode(city).latitude, geolocator.geocode(city).longitude) for city in cities]
+
+    df = pd.DataFrame(data, columns=["city", "latitudes", "longitude"])

    return df
<<<<<  bot-2b8c8332-5d21-4374-9afe-73264093067f  >>>>>
