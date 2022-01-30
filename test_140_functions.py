from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.typical_range_consistent() is True
    s.typical_range = (3.445,-2.3)
    assert s.typical_range_consistent() is False
    s.typical_range = None
    assert s.typical_range_consistent() is False

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()