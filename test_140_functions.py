"""Area for testing functions implemented by lab group 140"""
from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation
import pytest

def test_1D():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1_id = "test-s1-id"
    m1_id = "test-m1-id"
    label1 = "some station1"
    coord1 = (-1.0, 3.0)
    trange1 = (-1.3, 5.64)
    river1 = "River X1"
    town1 = "My Town1"
    s1 = MonitoringStation(s1_id, m1_id, label1, coord1, trange1, river1, town1)
    stations = [s, s1]

    assert rivers_with_station(stations) == ["River X", "River X1"]
    assert stations_by_river(stations) == {"River X": ["some station"], "River X1": ["some station1"]}
    stations[1].river = "River X"
    assert rivers_with_station(stations) == ["River X"]
    assert stations_by_river(stations) == {"River X": ["some station", "some station1"]}


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