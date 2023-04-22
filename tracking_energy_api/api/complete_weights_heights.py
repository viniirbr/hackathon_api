#%%
import os
import json
from collections import defaultdict
# %%
player_weights = defaultdict(bool)
player_heights = defaultdict(bool)
directory = r"ManCity Hackathon Json Files\ManCity Hackathon Json Files"
for filename in os.listdir(directory):
    if not filename.endswith("lineups.json"):
        print(f"Not {filename}")
        continue
    else:
        print(filename)
    f = os.path.join(directory, filename)
    with open(f) as lineups:
        data = json.load(lineups)
        #print(data)
        for lineup in data:
            for player in lineup["lineup"]:
                player_weights[player["player_name"]] = player["player_weight"] or None
                player_heights[player["player_name"]] = player["player_height"] or None
                #if player["player_weight"] is None:
                 #   player["player_name"])
print(player_weights)
# %%
[player for player, weight in player_weights.items() if weight is None]

# %%
player_weights_google = player_weights.copy()
player_weights_google['Yui Hasegawa']=47.0
player_weights_google['Giovana Queiroz Costa'] = 60.0
# for missing weights, estimate using average cm/kg
player_weights
# %%
len(player_weights_google) == len(player_heights)
no_height = [player for player, height in player_heights.items() if height is None]
player_heights
no_height
# %%
player_heights_google = player_heights.copy()
player_heights_google[no_height[0]] = 168.0
player_heights_google[no_height[2]] = 166.0
player_heights_google[no_height[3]] = 162.0
player_heights_google[no_height[6]] = 167.0
player_heights_google[no_height[7]] = 165.0
player_heights_google[no_height[8]] = 164.0
player_heights_google[no_height[11]] = 156.0
player_heights_google[no_height[12]] = 170.0
player_heights_google[no_height[13]] = 175.0
player_heights_google[no_height[16]] = 163.0
player_heights_google[no_height[17]] = 167.0
player_heights_google[no_height[18]] = 171.0
player_heights_google[no_height[22]] = 165.0
player_heights_google[no_height[23]] = 168.0
player_heights_google[no_height[24]] = 171.0
player_heights_google[no_height[25]] = 165.0
player_heights_google[no_height[26]] = 175.0
player_heights_google[no_height[26]] = 171.0
player_heights_google[no_height[31]] = 166.0
# %%
non_null_heights = [height for height in  player_heights_google.values() if height is not None]
average_height = sum(non_null_heights)/len(non_null_heights)


non_null_weights = [weight for weight in  player_weights_google.values() if weight is not None]
average_weight = sum(non_null_weights)/len(non_null_weights)

average_height,average_weight, average_weight/average_height
# %%
player_heights_inferred = player_heights_google.copy()
for player in player_heights_google.keys():
    player_heights_inferred[player] = player_heights_google[player] or average_height 

player_weights_inferred = player_weights_google.copy()
for player in player_weights_google.keys():
    player_height = player_heights_inferred[player]
    player_weights_inferred[player] = player_weights_google[player] or player_height * average_weight/average_height
# %%
player_heights_inferred
# %%
player_weights_inferred
# %%
