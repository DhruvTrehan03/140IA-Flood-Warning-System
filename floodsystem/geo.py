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
        