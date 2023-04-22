from data import city_brighton_tracking, city_leicester_tracking, city_liverpool_tracking, city_spurs_tracking, city_villa_tracking, players, complete_weights_and_heights
from pymongo import MongoClient
from mongo_connection import uri

client = MongoClient(uri)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client.ManHaysHack

col = db.tracking
col.delete_many({})
player_tracking = city_brighton_tracking() + city_leicester_tracking() + city_liverpool_tracking() + city_spurs_tracking()+ city_villa_tracking()

result = col.insert_many( player_tracking )
print(result.acknowledged)
players_info_col = db["players_info"]
players_info_col.delete_many({})
weights, heights = complete_weights_and_heights()
players_info, _ = players(weights, heights)
result = players_info_col.insert_many(players_info)
print(result.acknowledged)