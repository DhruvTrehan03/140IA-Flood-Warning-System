# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    station_list = []
    #from floodsystem.utils import sorted_by_key  
    for station in stations:
        distance = haversine(station.coord, p)
        station_list.append((station.name,station.town,distance))
    sorted_station = sorted_by_key(station_list, 2)
    return sorted_station

def stations_within_radius(stations, centre, r):
    radius = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
            radius.append(station.name)
    return sorted(radius)

# Task 1D
def rivers_with_station(stations):
    rivers_with_station = []
    for i in stations:
        if i.river not in rivers_with_station:
            rivers_with_station.append(i.river)
    return sorted(rivers_with_station)

# Task 1D
def stations_by_river(stations):
    river_stations = {}
    for i in stations:
        if i.river in river_stations.keys():
            river_stations[i.river].append(i.name)
        else:
            river_stations[i.river] = [i.name]
    for k in river_stations:
        sorted(river_stations[k])
    return river_stations

# Task 1E
def rivers_by_station_number(stations, N):
    
    # Check that N is a valid number of rivers
    if type(N) is not int:
        raise TypeError("Number of rivers must be an integer")
    if N < 1:
        raise ValueError("Number of rivers must be more than zero")
    
    # generate list of tuples for rivers and number of stations
    river_stations = stations_by_river(stations)
    station_numbers = []
    for k in river_stations.keys():
        station_numbers.append((k,len(river_stations[k])))
    
    # utilise function that has been prewritten in utils to sort in descending order
    station_numbers = sorted_by_key(station_numbers, 1)
    station_numbers.reverse()
    
    # retrieve top highest N rivers by station number, including joint equals
        # add first value to end to prevent index out of range errors
    station_numbers.append(station_numbers[0])
    while station_numbers[N-1][1] == station_numbers[N][1] and N < len(station_numbers)-1:
        N += 1

    print(N)
    return station_numbers[0:N]
        