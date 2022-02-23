from floodsystem.analysis import polyfit
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
def run():

    # Build list of stations
    stations = build_station_list()
    # Station name to find
    #station_name = [('Hayes Basin', 14.5)]
    station_name = stations_highest_rel_level(stations,5)
    dt = 2
    p = 3
    for i in range(len(station_name)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == station_name[i][0]:
                station_cam = station
                print (station_cam)
                break

        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(station_name[i]))
            return

        dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, p)
        plot_water_level_with_fit(station_cam,dates,levels, p) #call polyfit and plotting function



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()


