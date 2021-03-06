# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  
from haversine import haversine, Unit

# Task 1B

def stations_by_distance(stations, p):
    station_list = [] 
    for station in stations:
        distance = haversine(station.coord, p)
        station_list.append((station.name,station.town,distance))
    sorted_station = sorted_by_key(station_list, 2)
    return sorted_station

# Task 1C
def stations_within_radius(stations, centre, r):
    radius = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
            radius.append(station.name)
    return sorted(radius)

# Task 1D
def rivers_with_station(stations):
    """Returns a list of rivers that have monitoring stations on them
    Arguments: stations, a list of Monitoring station objects"""
    rivers_with_station = []
    for i in stations:
        if i.river not in rivers_with_station:
            rivers_with_station.append(i.river)
    return sorted(rivers_with_station)

# Task 1D
def stations_by_river(stations):
    """Returns a dictionary of rivers as keys, and a list of monitoring stations on that river 
    Arguments: stations, a list of Monitoring station objects"""
    river_stations = {}
    for i in stations:
        if i.river in river_stations.keys():
            river_stations[i.river].append(i.name)
        else:
            river_stations[i.river] = [i.name]
    for k in river_stations:
        river_stations[k].sort()
    return river_stations

# Task 1E
def rivers_by_station_number(stations, N):
    """Returns a number of rivers with the greatest number of monitoring stations
    Rivers with the same number of stations are returned, even beyond the chosen quantity
    Arguments: station, a list of Monitoring station objects; N, number of rivers to be returned"""
    river_stations = stations_by_river(stations)
    # Check that N is a valid number of rivers
    if type(N) is not int:
        raise TypeError("Number of rivers must be an integer")
    if N < 1:
        raise ValueError("Number of rivers must be more than zero")
    if N > len(river_stations):
        raise ValueError("Number of rivers asked for cannot exceed number of rivers")
    
    # generate list of tuples for rivers and number of stations
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

    return station_numbers[0:N]
        