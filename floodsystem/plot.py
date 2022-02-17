import matplotlib.pyplot as plt
import numpy as np
from .analysis import polyfit
import matplotlib

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

def plot_water_level_with_fit(station, dates, levels, p):
    high = np.full(( len(levels)), station.typical_range[0])
    low = np.full(( len(levels)), station.typical_range[1])
    date = matplotlib.dates.date2num(dates)

    p_coeff = np.polyfit(date - date[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(date[0], date[-1], 30)
    
    
    plt.plot(x1, poly(x1 - date[0]))
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