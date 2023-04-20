import numpy as np
from data import players, complete_weights_and_heights, city_brighton_tracking
from datetime import datetime

def mets(speed, weight, seconds = 0.04):
    # Intended to receive arrays of speeds 
    # Formula of mets(speed, weight, seconds=60) in miles/pounds https://tbonesbaseball.com/calculating-your-mets-for-running/#:~:text=The%20formula%20for%20calculating%20your,amount%20of%20energy%20at%20rest.
    # Recall that mets are a unit per minute
    #1 mile = 1609,34 meters
    #1 minute = 60 seconds
    #1 kg = 2,20462 pounds
    # potential research https://exrx.net/Aerobic/WalkCalExp and calculator https://exrx.net/Calculators/WalkRunMETs
    metersecond_to_milesminute = 1609.34 / 60 
    kg_to_pound = 2.20462
    METs = (0.0175 * metersecond_to_milesminute * speed) + (0.0001 * kg_to_pound * weight) 
    interval_mets = seconds * METs / 60
    return interval_mets

def calories_burnt(mets, weight):
    # Intended to receive an array of mets
    # formula https://marathonhandbook.com/what-are-mets/
    # time could be introduced here instead of in mets https://www.cmsfitnesscourses.co.uk/blog/using-mets-to-calculate-calories-burned/
    calories = (mets * 3.5 * weight ) / 200
    return np.sum(calories)

def energy_level(calories_burnt, calory_baseline = 2400, calory_start = 2000, recent_activity_factor = 1, recovery_factor = 0, previous_games_factor = 1):
    #default energy based on https://www.healthychildren.org/English/health-issues/injuries-emergencies/sports-injuries/Pages/Female-Athlete-Triad.aspx#:~:text=Most%20female%20athletes%20need%20a,help%20the%20athlete%20perform%20better!
    starting_energy = (1+recovery_factor)*calory_start*recent_activity_factor*previous_games_factor
    # For the second half we may introduce a recovery factor and the energy level at the end of the first half as discount
    # There can also be a discount for playing recently, that would be computed separatedly
    energy_level = (starting_energy - calories_burnt )/calory_baseline
    #a warning would be given when low energy, but not in this function
    #if np.any(energy_level <= 0):
    #    warnings.warn("Warning: run out of energy")
    return energy_level

def energy_level_of_player_in_game(db, ssiId, date, calory_baseline = 2400, calory_start = 2000, recent_activity_factor = 1, recovery_factor = 0, previous_games_factor = 1):
    col = db.tracking
    date = datetime.strptime(date,"%Y-%m-%d")
    my_doc = col.find_one({"match_date" : date, "ssiId": ssiId},{"_id":0, "speeds":1})
    if my_doc is not None:
        speeds1, speeds2 = my_doc["speeds"].values()
        weight_col = db.players_info
        weight, = weight_col.find_one({"ssiId": ssiId}, {"_id":0, "weight": 1}).values()
        speeds1, speeds2 = np.array([speed["speed"] for speed in speeds1]), np.array([speed["speed"] for speed in speeds2])

        mets1 = mets(speeds1, weight)
        calories1 = calories_burnt(mets1, weight)
        energy1 = energy_level(calories1, calory_start=calory_start, calory_baseline=calory_baseline)
        mets2 = mets(speeds2, weight)
        calories2 = calories_burnt(mets2, weight)
        energy2 = energy_level(calories2, recent_activity_factor=energy1, recovery_factor=recovery_factor, calory_start=calory_start, calory_baseline=calory_baseline)

        return energy2
    else:
        return "No match or player found"


# wrap in a class that contains the baseline, start and db, 