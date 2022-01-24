# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

#from utils import sorted_by_key  
from haversine import haversine, Unit
station_list = []
def stations_by_distance(stations, p):
    from floodsystem.utils import sorted_by_key  
    for station in stations:
        distance = haversine(station.coord, p)
        station_list.append((station.name,station.town,distance))
    sorted_station = sorted_by_key(station_list, 2)
    return sorted_station