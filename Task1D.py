from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Totals the number of rivers with at least one monitoring station, and prints the first 10 of these in alphabetical order"""
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print("There are {} stations with rivers, the first 10 of these alphabetically are {}".format(len(rivers),rivers[0:10]))
        
    river_stations = stations_by_river(stations)
    Aire_stations = river_stations["River Aire"]
    Cam_stations = river_stations["River Cam"]
    Thames_stations = river_stations["River Thames"]
    
    print("The River Aire has these monitoring stations {}, the River Cam these ones {}, and the River Thames these {}. All stations are listed in alphabetical order".format(Aire_stations,Cam_stations,Thames_stations))

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()