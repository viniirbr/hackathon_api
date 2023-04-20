from energy_calculator import mets, calories_burnt, energy_level, energy_level_of_player_in_game
from data import players, complete_weights_and_heights, city_brighton_tracking
import numpy as np
from datetime import datetime
from pymongo import MongoClient
from decouple import config



PASSWORD = config("PASSWORD")


def test_energy_from_python_data():
    weights, heights = complete_weights_and_heights()
    player_tracking = city_brighton_tracking()
    player_info, _ = players(weights, heights)
    #print(player_tracking[0]["match_date"])

    ssiId = "0746befc-a701-4b33-8faf-b3cccccf17bb"
    weight = next(filter(lambda x: x["ssiId"] == ssiId, player_info))["weight"]
    player = next(filter(lambda x: x["ssiId"] == ssiId, player_tracking))
    speeds1, speeds2 = player["speeds"].values()
    speeds1, speeds2 = np.array([speed["speed"] for speed in speeds1]), np.array([speed["speed"] for speed in speeds2])


    mets1 = mets(speeds1, weight)
    calories1 = calories_burnt(mets1, weight)
    energy1 = energy_level(calories1)
    #print(calories1)
    mets2 = mets(speeds2, weight)
    calories2 = calories_burnt(mets2, weight)
    energy2 = energy_level(calories2, recent_activity_factor=energy1, recovery_factor=0.2)

    print(energy1, energy2)

def test_energy_from_mongo():
    uri = "mongodb+srv://ja683:"+PASSWORD+"@cluster0.l2in6rm.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.ManHaysHack
    col = db.tracking
    ssiId = "0746befc-a701-4b33-8faf-b3cccccf17bb"
    date = datetime.strptime("2022-12-04","%Y-%m-%d")
    #my_doc = col.find({"match_date" : date, "ssiId": ssiId},{"speeds":1})
    #docs = list(my_doc)
    #print(docs[0].keys())
    #print(len(docs)==1)
    my_doc = col.find_one({"match_date" : date, "ssiId": ssiId},{"_id":0, "speeds":1})
    speeds1, speeds2 = my_doc["speeds"].values()
    weight_col = db.players_info
    weight, = weight_col.find_one({"ssiId": ssiId}, {"_id":0, "weight": 1}).values()
    print(weight)
    speeds1, speeds2 = np.array([speed["speed"] for speed in speeds1]), np.array([speed["speed"] for speed in speeds2])

    mets1 = mets(speeds1, weight)
    calories1 = calories_burnt(mets1, weight)
    energy1 = energy_level(calories1)
    print(calories1)
    mets2 = mets(speeds2, weight)
    calories2 = calories_burnt(mets2, weight)
    energy2 = energy_level(calories2, recent_activity_factor=energy1, recovery_factor=0.2)

    print(energy1, energy2)

def test_energy_calculator():
    uri = "mongodb+srv://ja683:"+PASSWORD+"@cluster0.l2in6rm.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.ManHaysHack
    ssiId = "0746befc-a701-4b33-8faf-b3cccccf17bb"
    date = "2022-12-04"
    final_energy_level = energy_level_of_player_in_game(db, ssiId, date, recovery_factor=0.2, calory_start=2000)
    return final_energy_level

print(test_energy_calculator())

