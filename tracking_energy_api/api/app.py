import json
from flask import Flask, request, jsonify
from datetime import datetime
from energy_calculator import energy_level_of_player_in_game, predict_time_to_threshold
from flask_pymongo import PyMongo
from mongo_connection import uri
from math import floor

from asgiref.sync import sync_to_async


app = Flask(__name__)
client = PyMongo(app, uri=uri)
@app.route('/')
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/energy', methods = ["GET"])
async def energy_calculation():
    ''' returns enery level as a number between 0 and 1 if the information is found, otherwise sends "No match or player found" message'''
    ssiId = request.args.get('ssiId')
    date = request.args.get('date') or datetime.strftime(datetime.now().date(), "%Y-%m-%d")
    db = client.db
    final_energy_level = await sync_to_async(energy_level_of_player_in_game)(db, ssiId, date, recovery_factor=0.2, calory_start=2000)
    response = final_energy_level or "No player or match found"
    return jsonify(response)

@app.route('/energy/predict', methods = ["GET"])
async def energy_prediction():
    ''' returns an estimated amount of minutes to reach a certain energy level from last data'''
    ssiId = request.args.get('ssiId')
    date = request.args.get('date') or datetime.strftime(datetime.now().date(), "%Y-%m-%d")
    try:
        threshold = float(request.args.get('threshold'))
    except:
        threshold = 0.5
    db = client.db
    energy_levels = await sync_to_async(energy_level_of_player_in_game)(db, ssiId, date, recovery_factor=0.2, calory_start=2000, cum = True)
    prediction = {"minutes" : floor(predict_time_to_threshold(energy_levels, threshold))} if energy_levels is not None else "No player or match found"
    return jsonify(prediction)


@app.route('/tracking', methods = ["POST"])
def add_tracking_data():
    content = request.get_json()
    #date = content.get("date") consider this in case we want to update a past game, otherwise add it to today
    date = content.get("date") or datetime.strftime(datetime.now().date(), "%Y-%m-%d")
    period = content["period"]
    time = content["gameClock"]
    players = content["homePlayers"]+content["awayPlayers"] #consider having a different collection for home players, maybe even a different collection for each team
    ids_speeds = dict([(player["playerId"], player["speed"]) for player in players])
    
    db = client.db
    col = db.tracking
    modified = 0
    for id,speed in ids_speeds.items():
        filter = {"ssiId" : id, "match_date" : date}
        update = {"$push": {"speeds.period_1":{"time": time, "speed":speed}}} if period == 1 else {"$push": {"speeds.period_1":{"time": time, "speed":speed}}}
        result = col.update_one(filter, update, upsert=True)
        modified += result.modified_count
    # if a time is repeated it will add it again, I don't know how to fix it without doing to much work so for now I'll leave it like this because the info is supposed to be new
    return jsonify(f"{modified} modified documents")#json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
   app.run(debug=True)