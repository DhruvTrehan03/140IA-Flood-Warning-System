from .station import MonitoringStation
from .utils import sorted_by_key
from .stationdata import update_water_levels


# Task 2B
def stations_level_over_threshold(stations, tol, ignore=False):
    if not (type(tol) is int or type(tol) is float):
        raise TypeError("The value for tolerance must be a number")
    update_water_levels(stations)
    station_levels = []
    for i in stations:
        ratio = i.relative_water_level()
        if ignore:
            if ratio is not None:
                station_levels.append((i.name,ratio))
        else:
            if ratio is not None and ratio > tol:
                station_levels.append((i.name,ratio))
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
