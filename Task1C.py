from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    centre = (52.2053,0.1218)
    assert isinstance(centre, tuple), 'Coordinate should be a tuple!'
    assert len(centre)==2, 'Not a Valid Coordinate, should be 2 coordinates'
    r=10
    # Print number of stations
    print(stations_within_radius(stations,centre,r))



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()