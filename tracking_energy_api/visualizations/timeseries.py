#%%
import json
import matplotlib.pyplot as plt
import warnings
import numpy as np

#%%
with open(r"C:\Users\Usuario\GitHub\MCHaysHack\MCI Women's Files\g2312135_SecondSpectrum_tracking-produced.jsonl") as jsons:
    jsons_list = list(map(json.loads, jsons.readlines()))
    time = []
    speed = []
    player_id = jsons_list[0]["homePlayers"][0]["optaId"]
    for j in jsons_list:
        time.append(j["gameClock"])
        speed.append(j["homePlayers"][0]["speed"])


#%%
second_half = time[1:].index(0)+1 #if there is additional time I may have to repeat this, consider using the periods
plt.plot(time[:second_half], speed[:second_half], label = "First period")
plt.plot(time[second_half:], speed[second_half:], label = "Second period")
plt.legend()
#plt.plot([time[0], time[-1]], [speed[0], speed[-1]])
#plt.plot(time[second_half:])
plt.xlabel("Time")
plt.ylabel("Speed")
plt.title(f"Opta Id: {player_id}")
#print(second_half, (time[:second_half])[-10:])
# %%
def mets(speed, weight, seconds = 0.04):
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
    # formula https://marathonhandbook.com/what-are-mets/
    # time could be introduced here instead of in mets https://www.cmsfitnesscourses.co.uk/blog/using-mets-to-calculate-calories-burned/
    calories = (mets * 3.5 * weight ) / 200
    return calories

def energy_level(calories_burnt, calory_baseline = 2400, calory_start = 2000, recent_activity_discount = 0):#, recovery_factor = 0):
    #default energy based on https://www.healthychildren.org/English/health-issues/injuries-emergencies/sports-injuries/Pages/Female-Athlete-Triad.aspx#:~:text=Most%20female%20athletes%20need%20a,help%20the%20athlete%20perform%20better!
    #starting_energy = calory_start - (recent_activity_discount - recovery_factor)*calory_start
    starting_energy = calory_start - recent_activity_discount*calory_start
    energy_level = (starting_energy - calories_burnt )/calory_baseline
    #if np.any(energy_level <= 0):
    #    warnings.warn("Warning: run out of energy")
    return energy_level
# %%
second_spectrum_name = "Y. Hasegawa"
second_spectrum_date = "2023-2-11"
FAWSL_date = "2023-02-11" #will need reformating
home_team_name = "Manchester City WFC" #abreviates to ManCity (create a dictionarty for this)
away_team_name = "Arsenal WFC" #abbreviates as Arsenal 
#I can use abreviations or just look at the lineups that match both fields
weight = "null" #in this cases maybe replace by average weight if there are enough values
google_weight = 47 # I can also fill with google values if I can

# %%
first_half_time = time[:second_half]
first_half_speed = speed[:second_half]
second_half_time = time[second_half:]
second_half_speed = speed[second_half:]

first_half_energy_comsuption = np.cumsum(list(map(lambda s: calories_burnt(mets(s, google_weight), google_weight), first_half_speed)))
first_half_energy_levels = energy_level(first_half_energy_comsuption, calory_start=1500)
plt.plot(first_half_time, first_half_energy_levels, label = "First half energy")

recovery = 0.2
second_half_energy_start = 1500*first_half_energy_levels[-1]*(1+recovery)
second_half_energy_comsuption = first_half_energy_comsuption[-1]  +np.cumsum(list(map(lambda s: calories_burnt(mets(s, google_weight), google_weight), second_half_speed)))
second_half_energy_levels = energy_level(second_half_energy_comsuption, calory_start=second_half_energy_start)

plt.plot(second_half_time, second_half_energy_levels, label = "Second half energy")
plt.legend()
#plt.ylim([0.9,1])
plt.ylabel(r"Energy level as a % of total energy")
plt.show()
# %%
