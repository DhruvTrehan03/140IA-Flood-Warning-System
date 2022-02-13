from .station import MonitoringStation
from .utils import sorted_by_key
from .stationdata import update_water_levels
# Task 2B
def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    station_levels = []
    for i in stations:
        ratio = i.relative_water_level()
        if ratio is not None and ratio > tol:
            station_levels.append((i.name,ratio))
    return sorted_by_key(station_levels, 1, True)

