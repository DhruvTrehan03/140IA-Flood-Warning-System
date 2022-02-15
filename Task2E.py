import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():

    # Build list of stations
    stations = build_station_list()
    # Station name to find
    station_name = stations_highest_rel_level(stations,5)
    dt = 10
    for i in range(len(station_name)):
    # Find station
        print (station_name[i])
        station_cam = None
        for station in stations:
            if station.name == station_name[i]:
                station_cam = station
                break

        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(station_name[i]))
            return

        dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station_cam, dates, levels)

        # Check that station could be found. Return if not found.


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()


