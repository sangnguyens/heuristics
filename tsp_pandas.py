import numpy as np
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd

def create_cities(*args):
    if args:
        return pd.DataFrame(args)
    else:
        return pd.DataFrame({
            "city": [
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Philadelphia",
                "Phoenix",
                "San Antonio",
                "San Diego",
                "Dallas",
                "San Jose",
            ],
            "latitudes": [
                40.7128,
                34.0522,
                41.8781,
                29.7604,
                39.9526,
                33.4484,
                29.4241,
                32.7157,
                32.7767,
                37.337,
            ],
            "longitude": [
                -74.0059,
                -118.2437,
                -87.6298,
                -95.3698,
                -75.2412,
                -112.074,
                -98.4936,
                -117.1611,
                -96.7979,
                -121.8863
            ]
        }
        )

def tsp(df):
    # create a new dataframe taht will hold the shortest path
    df_shortest = pd.DataFrame(columns=["city", "latitudes", "longitude"])
    # random select start city
    start_city = random.choice(list(df["city"]))
    # add the starting city to the shortest path
    df_shortest = df_shortest.append(df[df.city==start_city])
    # remove the starting city from original frame
    df =  df[df.city != start_city]
    # loop through the remaining cities until it is empty
    while not df.empty:
        # create a list of distances from the last city in the shortest path to each city in the original dataframe
        distances = []
        for index, row in df.iterrows():
            distance = np.sqrt(
                (row["latitudes"] - df_shortest.iloc[-1]["latitudes"])**2 \
                + (row["longitude"] - df_shortest.iloc[-1]["longitude"])**2
            )
            distances.append(distance)
        # find the index of the city in the original dataframe that is closest to the last city in the shortest path
        closest_city_index = distances.index(min(distances))