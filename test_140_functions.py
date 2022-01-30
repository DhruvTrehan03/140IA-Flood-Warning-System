from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
import pytest


def test_1E():
    stations = build_station_list()
    with pytest.raises(TypeError):
        rivers_by_station_number(stations, "e")
    with pytest.raises(ValueError):
        rivers_by_station_number(stations, 0)
    with pytest.raises(ValueError):
        rivers_by_station_number(stations, -1)
    
def test_1F():
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

