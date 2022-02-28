import datetime
import matplotlib
import numpy as np
from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_under_threshold, stations_lowest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit


def run():
    stations = build_station_list()
    update_water_levels(stations)
    low_moderate = stations_level_under_threshold(stations,1) # Water levels are within the typical range so flood risk is low,
    low, moderate = [], []                                                          # unless levels are increasing
    dt = 2
    p = 3
    for i in range(len(low_moderate)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == low_moderate[i][0]:
                station_cam = station
                break

        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(low_moderate[i]))
            return

        dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, p)
        
        date = matplotlib.dates.date2num(dates)
        x1 = np.linspace(date[0], date[-1], 30)
        
        low_moderate_rate = 0.05 # set the maximum increase rate for flood risk to be considered low still
        
        diff = np.diff(poly(x1-date[0]))    # differentiating the polyfit function and evaluate for average gradient before comparing
        gradient = sum(diff)/len(diff)
        if gradient <low_moderate_rate:
            low.append(station_cam.name)
        if gradient >low_moderate_rate:
            moderate.append(station_cam.name)
    
    print("The stations at low risk are {}".format(low))
    print("The stations at moderate risk are {}".format(moderate))
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()