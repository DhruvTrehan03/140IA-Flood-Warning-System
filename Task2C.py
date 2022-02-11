from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    highestN = stations_highest_rel_level(stations,0)
    for i in highestN:
        print(i)
    

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()