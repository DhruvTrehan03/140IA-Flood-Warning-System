from distutils.command.build import build
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Checks the monitoring station data for inconsistencies in typical range,
     and returns a sorted list of stations with inconsistent typical ranges"""
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))




if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()