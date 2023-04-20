from collections import defaultdict
from datetime import datetime
import json
import os


def complete_weights_and_heights(option="inferred"):
    player_weights = defaultdict(bool)
    player_heights = defaultdict(bool)
    directory = r"ManCity Hackathon Json Files\ManCity Hackathon Json Files"
    for filename in os.listdir(directory):
        if not filename.endswith("lineups.json"):
            continue
        f = os.path.join(directory, filename)
        with open(f) as lineups:
            data = json.load(lineups)
            for lineup in data:
                for player in lineup["lineup"]:
                    player_weights[player["player_name"]] = player["player_weight"] or None
                    player_heights[player["player_name"]] = player["player_height"] or None
    if option not in ["google", "inferred"]:
        return player_weights, player_heights 
    
    player_weights_google = player_weights.copy()
    player_weights_google['Yui Hasegawa']=47.0
    player_weights_google['Giovana Queiroz Costa'] = 60.0

    no_height = [player for player, height in player_heights.items() if height is None]
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

    if option == "google":
        return player_weights_google, player_heights_google
    
    non_null_heights = [height for height in  player_heights_google.values() if height is not None]
    average_height = sum(non_null_heights)/len(non_null_heights)


    non_null_weights = [weight for weight in  player_weights_google.values() if weight is not None]
    average_weight = sum(non_null_weights)/len(non_null_weights)

    player_heights_inferred = player_heights_google.copy()
    for player in player_heights_google.keys():
        player_heights_inferred[player] = player_heights_google[player] or average_height 

    player_weights_inferred = player_weights_google.copy()
    for player in player_weights_google.keys():
        player_height = player_heights_inferred[player]
        player_weights_inferred[player] = player_weights_google[player] or player_height * average_weight/average_height
    
    return player_weights_inferred, player_heights_inferred
   
    



def players(weights, heights):
    weights, heights = complete_weights_and_heights()
    players = []
    names = list(weights.keys())
    directory = r"MCI Women's Files"
    players_meta = []
    for filename in os.listdir(directory):
        if not filename.endswith("meta.json"):
            continue
        f = os.path.join(directory, filename)
        with open(f) as meta:
            data = json.load(meta)
            players_meta = players_meta + data["homePlayers"]+data["awayPlayers"]
    playersSet = list({v["ssiId"]: v for v in players_meta}.values())
    for player in playersSet:
            player_data = {"name": player["name"], "ssiId": player["ssiId"], "optaId": player["optaId"]}
            for name in names:
                if coincidence(name, player["name"]):
                    player_data["weight"] = weights[name]
                    player_data["height"] = heights[name]
                    player_data["whole name"] = name
                    names.remove(name)
                    break        
            else:
                player_data["weight"], player_data["height"], names = exceptions(player["name"], weights, heights, names)
                
            players.append(player_data)
                
    return players, names

def coincidence(whole_name, short_name):
    whole_parts = whole_name.split(" ")
    short_parts = short_name.split(" ")
    good_format_coincidence = ((whole_parts[0][0] == short_parts[0][0]) and (whole_parts[-1].lower() == short_parts[-1].lower()))
    bad_format_coincidence = set(whole_parts).intersection(set(short_parts))
    return True if good_format_coincidence or bad_format_coincidence else False

def exceptions(player_name, weights, heights, names):
    if player_name == "L. Walti":
        whole_name = "Lia WÃ¤lti"   
    elif player_name == "R. Dali":
        whole_name = "Rachel Daly"
    elif player_name == 'L. Geum-min':
        whole_name = 'Geum-Min Lee'
    elif player_name == 'J. Zigiotti Olme':
        whole_name = 'Julia Zigiotti-Olme'
    elif player_name == 'Y. Daniels':
        whole_name = 'Yana DaniÃ«ls'
    else:
        return None, None, names
    weight = weights[whole_name]
    height = heights[whole_name] 
    names.remove(whole_name)
    return weight, height, names


def check_names():
    weights, heights = complete_weights_and_heights()
    player_data, bad_format_names = players(weights, heights) #there are some names with different format and encoding that should be handled by hand
    return player_data, bad_format_names
#print(player_data)
#print(bad_format_names)
#walti = list(filter(lambda dic: "lti" in dic["name"], player_data))[0] #dictionary containing walti
#daly = list(filter(lambda dic: "R." in dic["name"], player_data))
#lee = list(filter(lambda dic: "-" in dic["name"], player_data))
#julia = list(filter(lambda dic: "J." in dic["name"], player_data))
#yana = list(filter(lambda dic: "Y." in dic["name"], player_data))
#print(yana)

#print(list(filter(lambda dic: "lti" in dic["name"], player_data)))
#print(list(filter(lambda name: "lti" in name, weights.keys())))
#print([player["short_name"] for player in player_data if ("name" not in player.keys())])
#print(len([player["name"] for player in player_data if ("name" in player.keys())]))
#print(coincidence("Kerstin Yasmijn Casparij", 'K. Casparij'))
#next:
#  games: game_id, date, players (so that I can more easily create the next one)? (by hand because there are few and is easier this way)
#  player_tracking: game_id (introduced by hand) player ssiId, optaId chosen from players and speeds = {period:[gameClock:speed]} from tracking

def game_tracking_data(path_meta, path_tracking, game_data):
    players_tracking = []
    game_data["match_date"] = datetime.strptime(game_data["match_date"],"%Y-%m-%d")
    with open(path_meta) as meta:
        data = json.load(meta)
        home_players = data["homePlayers"]
        away_players = data["awayPlayers"]
        game_players = home_players + away_players

    tracking_data = []
    with open(path_tracking) as tracking:
        jsons_list = list(map(json.loads, tracking.readlines()))
        for json_data in jsons_list:
            d = {"period" : int(json_data["period"]), "time" : json_data["gameClock"], 
             "players_speed" : [{"ssiId" : p["playerId"], "optaId" : p["optaId"],"speed" : p["speed"]} for p in json_data["homePlayers"]+json_data["awayPlayers"]]}
            tracking_data.append(d)

    for game_player in game_players:
        ssiId = game_player["ssiId"]
        #game_player_data = list(filter(lambda x: x["ssiId"] == ssiId, player_data))[0]
        speeds_1 = []
        speeds_2 = []
        for info in tracking_data:
            speed = list(filter(lambda x: x["ssiId"] == ssiId, info["players_speed"]))
            if not speed:
                break
            speed = speed[0]["speed"]
            speed_data = {"time":info["time"], "speed": speed}
            if info["period"] == 1:
                speeds_1.append(speed_data)
            else:
                speeds_2.append(speed_data)
        else:
            player_speed = {"ssiId" : ssiId, "speeds": {"period_1": speeds_1, "period_2": speeds_2}}
            player_tracking = game_data | player_speed
            players_tracking.append(player_tracking)
            continue
    
    return players_tracking

def city_leicester_tracking():
    path_meta = r"MCI Women's Files\g2312135_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312135_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3852832,
        "match_date" : "2023-02-11"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking

def city_leicester_tracking():
    path_meta = r"MCI Women's Files\g2312152_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312152_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3855947,
        "match_date" : "2022-10-16"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking

def city_brighton_tracking():
    path_meta = r"MCI Women's Files\g2312183_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312183_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3855980,
        "match_date" : "2022-12-04"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking

def city_liverpool_tracking():
    path_meta = r"MCI Women's Files\g2312166_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312166_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3855961,
        "match_date" : "2022-10-30"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking
    
def city_villa_tracking():
    path_meta = r"MCI Women's Files\g2312201_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312201_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3856030,
        "match_date" : "2023-01-21"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking
        
def city_spurs_tracking():
    path_meta = r"MCI Women's Files\g2312213_SecondSpectrum_meta.json"
    path_tracking = r"MCI Women's Files\g2312213_SecondSpectrum_tracking-produced.jsonl"
    game_data = {
        "match_id" : 3856040,
        "match_date" : "2023-03-05"}
    players_tracking = game_tracking_data(path_meta, path_tracking, game_data)   
    return players_tracking

#city_spurs_data = city_spurs_tracking()
#print(city_spurs_data)

#ADD POSITION TO PLAYER INFO
#STORE ENERGY AT EACH GIVEN TIME TO ALLOW REGRESSION
