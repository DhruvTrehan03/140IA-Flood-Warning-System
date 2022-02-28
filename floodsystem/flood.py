from .station import MonitoringStation
from .utils import sorted_by_key
from .stationdata import update_water_levels
from .datafetcher import fetch_measure_levels
import datetime

# Task 2B
def stations_level_over_threshold(stations, tol, ignore=False):
    if not (type(tol) is int or type(tol) is float):
        raise TypeError("The value for tolerance must be a number")
    update_water_levels(stations)
    station_levels = []
    for i in stations:
        ratio = i.relative_water_level()
        if i.name == "Letcombe Bassett":
            break
        else:
            if ignore:
                if ratio is not None:                   
                    station_levels.append((i.name,ratio))                                        
            else:
                if ratio is not None and ratio >= tol: 
                    station_levels.append((i.name,ratio))                                           
    return sorted_by_key(station_levels, 1, True)
# try:
#     dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))  
# except KeyError:
#     break    
# if levels:                                                                           
#     station_levels.append((i.name,ratio))   
# Task 2C
def stations_highest_rel_level(stations, N):
    if not type(N) is int:
        raise TypeError("The highest N stations wanted must be a number")
    if N < 1:
        raise ValueError("The highest N stations wanted must be at least 1")
    update_water_levels(stations)
    vals = stations_level_over_threshold(stations, 0, True)
    return vals[:N]
# Task 2G
def stations_level_under_threshold(stations, tol, ignore=False):
    dt =1
    if not (type(tol) is int or type(tol) is float):
        raise TypeError("The value for tolerance must be a number")
    update_water_levels(stations)
    station_levels = []
    for i in stations:
        ratio = i.relative_water_level()
        if i.name == "Letcombe Bassett":
            break
        else:
            if ignore:
                if ratio is not None:                   
                    station_levels.append((i.name,ratio))                                        
            else:
                if ratio is not None and ratio < tol: 
                    station_levels.append((i.name,ratio))                                           
    return sorted_by_key(station_levels, 1, False)

def stations_lowest_rel_level(stations, N):
    if not type(N) is int:
        raise TypeError("The lowest N stations wanted must be a number")
    if N < 1:
        raise ValueError("The lowest N stations wanted must be at least 1")
    update_water_levels(stations)
    vals = stations_level_under_threshold(stations, 0, True)
    return vals[:N]    
                                           