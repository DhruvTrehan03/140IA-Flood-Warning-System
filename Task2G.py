import datetime
import matplotlib
import numpy as np
from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_under_threshold, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit


def run():
    """Presents a list of towns in 4 categories, low risk, moderate risk, high risk, and severe risk of flooding. If a station has relative
    water levels lower than two thirds or above two thirds and decreasing, its town has no risk. If a station has relative water levels between
    two thirds and one which are constant or increasing by less than 0.10 per hour on average, or between 1 and 1.5 but decreasing its town 
    has low risk. If a town has relative water levels between two thirds and 1 and increasing by more than 0.10 per hour, or 1 and 1.5 which 
    are constant or increasing by less than 0.10 per hour, or between 1.5 and 2.5 which are decreasing its town has a moderate risk of flooding.
    If a town has relative water levels between 1 and 1.5 which are increasing by more than 0.10 per hour, or 1.5 and 2.5 which are constant or
    decreasing, or more than 2.5 but decreasing its town has a high risk of flooding. If a monitoring station has relative water levels between
    1.5 and 2.5 and increasing, or more than 2.5 it has a severe risk of flooding."""
    stations = build_station_list()
    update_water_levels(stations)
    
    safe_grad = 0
    limit_grad = 0.10

    no_risk = []
    low_risk = []
    moderate_risk = []
    high_risk = []
    severe_risk = []

    none_risk = stations_level_under_threshold(stations,0.67) # If water levels are below two thirds of the typical range there is no flooding risk
    for i in range(len(none_risk)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == none_risk[i][0]:
                station_cam = station
                break
        if not station_cam:
            print("Station {} could not be found".format(none_risk[i]))
            return

        if station_cam.town not in none_risk:
            try:
                no_risk.append(station_cam.town)
            except:
                pass
    
    # Produce towns at low risk
    low = stations_level_over_threshold(stations,0.67) # Check for stations above the low risk threshold, before using the level behaviour
                                                            # to determine if they are still low risk                                
    dt = 2                                                       
    p = 3
    levels_behaviour = {} # store water level gradient (prediction) to lower number of times polyfit used
    for i in range(len(low)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == low[i][0]:
                station_cam = station
                break
        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(low[i]))
            return
        
        # Produce polyfit functions and get gradients for stations not already low_risk
        dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) > len(levels):    
            dates_corrected = dates[:len(levels)]
            poly, d0 = polyfit(dates_corrected, levels, p)
            date = matplotlib.dates.date2num(dates_corrected)
        else:
            poly, d0 = polyfit(dates, levels, p)
            date = matplotlib.dates.date2num(dates)
        if len(date)>0:    
            x1 = np.linspace(date[0], date[-1], 30)
            diff = np.diff(poly(x1-date[0])) # differentiating the polyfit function and evaluate for average gradient before comparing
        else:
            diff = station_cam.typical_range[1]
   
        try:
            gradient = sum(diff)/len(diff)
        except TypeError:
            gradient = 0 # level assumed constant if no data available
        levels_behaviour[station_cam.name] = gradient # store gradient values to save time on the high risk checks

        # Comparison with values as selected for assigning risk
        if gradient < safe_grad:
            if station_cam.town not in none_risk:
                try:
                    none_risk.append(station_cam.town)
                except:
                    pass
        elif gradient > safe_grad and gradient < limit_grad:
            if station_cam.town not in low_risk:
                try:
                    low_risk.append(station_cam.town)
                except:
                    pass
        elif gradient > limit_grad:
            if station_cam.town not in moderate_risk:
                try:
                    moderate_risk.append(station_cam.town)
                except:
                    pass
    # Produce towns at moderate risk
    moderate = stations_level_over_threshold(stations,1)
    for i in range(len(moderate)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == moderate[i][0]:
                station_cam = station
                break
        if not station_cam:
            print("Station {} could not be found".format(moderate[i]))
            return

        # Comparison with values as selected for assigning risk
        if levels_behaviour[moderate[i][0]] < safe_grad:
            if station_cam.town not in low_risk:
                try:
                    low_risk.append(station_cam.town)
                except:
                    pass
        elif levels_behaviour[moderate[i][0]] > safe_grad and levels_behaviour[moderate[i][0]] < limit_grad:
            if station_cam.town not in moderate_risk:
                try:
                    moderate_risk.append(station_cam.town)
                except:
                    pass
        elif levels_behaviour[moderate[i][0]] > limit_grad:
            if station_cam.town not in high_risk:
                try:
                    high_risk.append(station_cam.town)
                except:
                    pass
    
    # Produce towns at high risk
    high = stations_level_over_threshold(stations,1.5)
    for i in range(len(high)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == high[i][0]:
                station_cam = station
                break
        if not station_cam:
            print("Station {} could not be found".format(high[i]))
            return

        # Comparison with values as selected for assigning risk
        if levels_behaviour[high[i][0]] <safe_grad:
            try:
                moderate_risk.append(station_cam.town)
            except:
                pass
        elif levels_behaviour[high[i][0]] > safe_grad and levels_behaviour[high[i][0]] < limit_grad:
            try:
                high_risk.append(station_cam.town)
            except:
                pass
        elif levels_behaviour[high[i][0]] > limit_grad:
            try:
                severe_risk.append(station_cam.town)
            except:
                pass
    
    # Produce towns at severe risk
    severe = stations_level_over_threshold(stations,1.5)
    for i in range(len(severe)):
    # Find station
        station_cam = None
        for station in stations:
            if station.name == severe[i][0]:
                station_cam = station
                break
        if not station_cam:
            print("Station {} could not be found".format(severe[i]))
            return

        # Comparison with values as selected for assigning risk
        if levels_behaviour[severe[i][0]] <safe_grad:
            try:
                high_risk.append(station_cam.town)
            except:
                pass
        else:
            try:
                severe_risk.append(station_cam.town)
            except:
                pass


    for i in severe_risk: # remove reapeated towns if there are any, to avoid a town being reported low risk due to one station,
        try:              # and moderate risk at another station for example
            high_risk.remove(i)
            moderate_risk.remove(i)
            low_risk.remove(i)
            none_risk.remove(i)
        except:
            pass
    for i in high_risk:
        try:
            moderate_risk.remove(i)
            low_risk.remove(i)
            none_risk.remove(i)
        except:
            pass
    for i in moderate_risk:
        try:
            low_risk.remove(i)
            none_risk.remove(i)
        except:
            pass            
    for i in low_risk:
        try:
            none_risk.remove(i)
        except:
            pass

    print("There are {} towns at low risk of flooding, these are {}".format(len(low_risk),low_risk))
    print("There are {} towns at moderate risk of flooding, these are {}".format(len(moderate_risk),moderate_risk))
    print("There are {} towns at high risk of flooding, these are {}".format(len(high_risk),high_risk))
    print("There are {} towns at severe risk of flooding, these are {}".format(len(severe_risk), severe_risk))
    risks = {"no risk": none_risk, "low risk":low_risk, "moderate risk": moderate_risk, "high risk": high_risk, "severe risk": severe_risk}
    
    # Ask if information on a specific town is wanted
    while True:
        choice = str(input("Would you like to search for a specific town (y/n)?"))
        if choice == "n" or choice == "N":
            break
        elif choice == "y" or choice == "Y":
            town_choice = str(input("What town would you like to search for"))
            for i in risks:
                for j in risks[i]:
                    if town_choice == j:
                        print("The town you chose, {}, has (a) {} of flooding".format(j,i))
        else:
            print("Please choose an option y or n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()