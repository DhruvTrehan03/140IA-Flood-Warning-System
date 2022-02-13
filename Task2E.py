import datetime
import matplotlib.pyplot as plt

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list



def run():

    # Build list of stations
    stations = build_station_list()
    # Station name to find
    station_name = ("Cam", "Bridgnorth", "Belmont", "Hookagate", "Eversley")

    for i in range(len(station_name)):
        # Find station
        station_cam = None
        for station in stations:
            if station.name == station_name[i]:
                station_cam = station
                break

        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(station_name[i]))
            return

        dt = 2
        dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))

        # # Print level history
        for date, level in zip(dates, levels):
            plt.plot(dates, levels) 
            #print(date, level)

 
    # Plot


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("High Risk Stations")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
