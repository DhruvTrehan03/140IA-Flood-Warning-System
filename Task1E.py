from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Prints the first 9 rivers, by the largest number of monitoring stations on those rivers 
    joint equals are included beyond 9"""
    stations = build_station_list()
    print(rivers_by_station_number(stations, 9))



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()