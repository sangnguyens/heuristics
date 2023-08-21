#!/usr/bin/env python

"""
This is a command-line tool that figures out the shortest distance to visit all cities in a list.
"""

import pandas as pd
import geopy
import geopy.distance
import random
import click

# build a function that takes variable length of strings and returns a list of cities
def my_cities(*args):
    """Build a list of cities from input"""
    return list(args)

def create_cities_dataframe(cities=None):
    """Create a pandas dataframe of cities and their latitudes and longitudes"""

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
            "Philadelphia",
            "Washington",
            "Portland",
            "Salt Lake City",
            "Oklahoma City",
            "Minneapolis",
            "Las Vegas",
            "Detroit",
            "Kansas City",
            "Nashville",
            "Memphis",
            "Columbus",
            "El Paso",
            "Charlotte",
        ]

    geolocator = geopy.geocoders.Nominatim(user_agent='tsp_pandas')

    data = [(city, geolocator.geocode(city).latitude, geolocator.geocode(city).longitude) for city in cities]

    return pd.DataFrame(data, columns=["city", "latitudes", "longitude"])

def tsp(cities_df):
    """Traveling Salesman Problem using pandas and Geopy"""

    # create a list of cities
    city_list = cities_df['city'].to_list()

    # shuffle the list to randomize the order of the cities
    random.shuffle(city_list)
    print(f"Randomized list of cities: {city_list}")

    # create a list of distances
    distances_list = []

    # loop through the list of cities using zip and modulo operator
    for city, next_city in zip(city_list, city_list[1:] + [city_list[0]]):
        # get the current city and next city
        current_city = cities_df[cities_df['city'] == city]
        next_city = cities_df[cities_df['city'] == next_city]

        # get the distance between the current city and the next city
        distance = geopy.distance.distance(
            (current_city['latitudes'].values[0], current_city['longitude'].values[0]),
            (next_city['latitudes'].values[0], next_city['longitude'].values[0]),
        ).miles
        # append the distance to the list of distances
        distances_list.append(distance)

    # return the sum of the distance list and the city list
    total_distance = sum(distances_list)

    return total_distance, city_list

def main(count, df=None):
    """Main function that runs the tsp simulation multiple times and returns the best result"""
    # create a list to hold the distances
    distances_list = []
    # create a list to hold the cities
    city_list_list = []
    # loop through the simulation
    if df is None:
        cdf = create_cities_dataframe()
    else:
        cdf = df
    for i in range(count): # run the simulation x time
        # get the distance and cities
        distance, city_list = tsp(cdf)
        print(f"Running simulation: {i}: Found total distance: {distance}")

        # append the distance to the list of distances
        distances_list.append(distance)
        # append the cities to the list of cities
        city_list_list.append(city_list)
    # get the index of the shortest distance
    shortest_distance_index = distances_list.index(min(distances_list))
    # print out the shortest distance
    print("Shortest distance: {}".format(min(distances_list)))
    # print the cities visited
    print("Cities visited: {}".format(city_list_list[shortest_distance_index]))

# create click group
@click.group()
def cli():
    """This is a command-line tool that figures out the shortest distance to visit all cities in a list."""

# create click command that takes a variable of arguments of cities passed in
@cli.command("cities")
@click.argument("cities", nargs=-1)
@click.option("--count", default=10, help="The number of times to run the simulation")
def cities_cli(cities, count):
    """This is a command-line tool that figures out the shortest distance to visit all cities in a list.
    Examle: ./fetch_cities_lat_long.py cities "New York" "Knoxville" --count 2
    """
    # create a list of cities
    city_list = my_cities(*cities)
    # create a pandas dataframe of cities and their latitudes and longitudes
    cities_df = create_cities_dataframe(city_list)
    # run the tsp simulation
    main(count, cities_df)

# add click command that runs the simulation x times
@cli.command("simulate")        
@click.option("--count", default=10, help="The number of times to run the simulation")
def simulate(count):
    """Run the simulation x times and print the shortest distance and cities visited.

    Example: ./fetch_cities_lat_long.py simulate --count 15

    """

    print(f"Running simulation: {count} times")
    main(count)

if __name__ == "__main__":
    cli()

# run the main function
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
