import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    date = matplotlib.dates.date2num(dates)
    try:    
        p_coeff = np.polyfit(date-date[0], levels, p)
        poly = np.poly1d(p_coeff)
        dtheta = date[0]
        return poly, dtheta
    except IndexError as err:
        print(err)
        print("No data available so assumed water levels constant")
        poly = np.poly1d([1,0])
        return poly

