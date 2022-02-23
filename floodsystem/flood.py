from .station import MonitoringStation
from .utils import sorted_by_key
from .stationdata import update_water_levels
from .datafetcher import fetch_measure_levels
import datetime

# Task 2B
def stations_level_over_threshold(stations, tol, ignore=False):
    dt =1
    if not (type(tol) is int or type(tol) is float):
        raise TypeError("The value for tolerance must be a number")
    update_water_levels(stations)
    station_levels = []
    for i in stations:
        ratio = i.relative_water_level()
        if ignore:
            if ratio is not None:
                try:
                    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))  #fetch level data from the past day
                except KeyError:
                    break                                                                               # if there is an error in fetching data, skip the error causing station
                if levels:
                    station_levels.append((i.name,ratio))                                               # add the station to the list if it has values for the past day (it isn't broken)
        else:
            if ratio is not None and ratio > tol:
                try:
                    dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))  #fetch level data from the past day
                except KeyError:
                    break                                                                               # if there is an error in fetching data, skip the error causing station
                if levels:
                    station_levels.append((i.name,ratio))                                               # add the station to the list if it has values for the past day (it isn't broken)
    return sorted_by_key(station_levels, 1, True)

# Task 2C
def stations_highest_rel_level(stations, N):
    if not type(N) is int:
        raise TypeError("The highest N stations wanted must be a number")
    if N < 1:
        raise ValueError("The highest N stations wanted must be at least 1")
    update_water_levels(stations)
    vals = stations_level_over_threshold(stations, 0, True)
    return vals[:N]


