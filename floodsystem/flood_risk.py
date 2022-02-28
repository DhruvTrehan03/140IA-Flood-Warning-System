import datetime
import matplotlib
import numpy as np
from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_under_threshold, stations_lowest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def low_risk(stations):
    low = stations_level_under_threshold(stations,0.67) # If water levels are below two thirds of the typical range flooding risk is low
    low_risk = []
    for i in range(len(low)):
        station_cam = None
        for station in stations:
            if station.name == low[i][0]:
                station_cam = station
                break
        try:
            low_risk.append(station_cam.town)
        except:
            pass