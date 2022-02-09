from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    p = (52.2053,0.1218)
    "Check the coordinate given is a tuple with 2 values"
    assert isinstance(p, tuple), 'Coordinate should be a tuple!'
    assert len(p)==2, 'Not a Valid Coordinate, should be 2 coordinates'
    print("Closest 10:", stations_by_distance(stations,p)[:10])
    print("Furthest 10:", stations_by_distance(stations,p)[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
