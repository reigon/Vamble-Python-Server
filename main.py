from youtubesearchpython.__future__ import *
import asyncio
from flask import Flask, jsonify, request
import os
from helpers.decorators import PerformaceTester
from service.youservice import YouService



 

videosSearch = None

app = Flask(__name__)

@app.route("/channel/list")
@PerformaceTester
def channelList():
    q = request.args.get('q')
    response = asyncio.run(YouService.channelListService( query = q))
    return jsonify(response), 200
    
@app.route("/channel/list/lite")
@PerformaceTester
def channelListLite():
    global videosSearch
    if request.args.get('new') == "1" or videosSearch is None:
        videosSearch = VideosSearch(request.args.get('q'), limit = 20)
        response = asyncio.run(YouService.channelListLiteService(videosSearch))
    else:
        response = asyncio.run(YouService.channelListLiteService(videosSearch))
    return jsonify(response), 200

@app.route("/channel/details")
def channelDetails():
    q = request.args.get('q')
    id = request.args.get('id')
    response = asyncio.run(YouService.channelDetailsService(query = q, 
                                                channelId = id))
    return jsonify(response), 200

@app.route("/test")
def test():
    # mongoCluster = pymongo.MongoClient("mongodb+srv://kaanakyuz:Skywalker1994!@vamblecluster.hc4nf.mongodb.net/")     
    # # print(mongodb.list_database_names)
    # db = mongoCluster["myFirstDatabase"]
    # channels = db["channels"].find()
    # chanelIds =  str(list(map(lambda x: x["channelId"], channels)))
    # return chanelIds, 200
    return

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))