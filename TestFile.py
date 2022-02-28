from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib
import numpy as np

def run():
    stations = build_station_list()
    print(len(stations))
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()