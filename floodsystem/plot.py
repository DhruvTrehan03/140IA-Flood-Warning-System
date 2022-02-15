import matplotlib.pyplot as plt
import numpy as np

def plot_water_levels(station, dates, levels):
    high = np.full(( len(levels)), station.typical_range[0])
    low = np.full(( len(levels)), station.typical_range[1])
    plt.plot(dates, levels) 
    plt.plot(dates,high)
    plt.plot(dates,low)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    # # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
