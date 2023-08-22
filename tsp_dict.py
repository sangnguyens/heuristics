#!/usr/bin/python3

import random

def tsp(cities):
    # create a list of cities
    city_list = list(cities.keys())
    # shuffle the list to randomize the order of the cities
    random.shuffle(city_list)
    # create a list of distance
    # distances_list = []
    # loop through the list
    distances_list = [cities[city_list[i]][city_list[i+1]] for i in range(len(city_list)) if i != len(city_list) - 1]
    distances_list.append(cities[city_list[len(city_list) - 1]][city_list[0]])
    # for i in range(len(city_list)):
    #     # if i is not the last city in the list
    #     if i != len(city_list) - 1:
    #         distance = cities[cities[i][city_list[i+1]]]
    #         distances_list.append(distance)
    #      # if i is the last item in the list
    #     else:
    #         # get the distance betwween the current city and first city
    #         distance = cities[cities[i][city_list[0]]]
    #         distances_list.append(distance)
    print(distances_list)
    # # return the sum of the distance list and the city list
    return sum(distances_list), city_list

# main function
def main():
    # create a dictionary of 10 cities  of American cities and their distances from each otehr
    cities = {
        "New York": {
            "New York": 0,
            "Chicago": 800,
            "Denver": 1400,
            "Los Angeles": 2100,
        },
        "Chicago": {
            "New York": 800,
            "Chicago": 0,
            "Denver": 600,
            "Los Angeles": 1300,
        },
        "Denver": {
            "New York": 1400,
            "Chicago": 600,
            "Denver": 0,
            "Los Angeles": 700,
        },
        "Los Angeles": {
            "New York": 2100,
            "Chicago": 1300,
            "Denver": 700,
            "Los Angeles": 0,
        },
    }

    # call the tsp function and unpack the return value
    distance, city_list = tsp(cities)

    # print the distance and cities
    print("The distance is {} and the city list is {}:".format(distance, city_list))

    return distance, city_list

def run():
    # create a list of distance
    distances_list = [main()[0][i] for i in range(len(100))]
    # create a list of cities
    city_list = [main()[1][i] for i in range(len(100))]
    # loop over 100 times
    # for _ in range(100):
    #     # call the main function
    #     distance, cities = main()
    #     # append the distance to the list of distances
    #     distances_list.append(distance)
    #     # append the cities to the list of cities
    #     city_list.append(cities)
    # get the index of the shortest distance
    index = distances_list.index(min(distances_list))
    # print out the shortest distance
    print("Shortest distance: {}, city tour {}".format(min(distances_list), city_list[index]))


if __name__ == "__main__":
    run()