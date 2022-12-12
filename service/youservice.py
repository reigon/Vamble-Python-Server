
import time
from youtubesearchpython.__future__ import *
from helpers import constants
import asyncio
from api.youapi import YouApi
from helpers.decorators import PerformaceTester
from helpers.helper import Helper
import pymongo


class YouService:
    
    async def channelListLiteService(videosSearch: VideosSearch): 
        
        youApi = YouApi()
        videos = await youApi.videoSearch(videosSearch)
        channelList = {}
        for video in videos:
            channelId = video['channel']["id"]
            channelList[channelId] = {"information": {}, "videos": []}
            channelList[channelId]["videos"].append(Helper.parseVideoInformation(video))
        return channelList
    
    async def channelListService( query: str):


        searchCounter = 0
        videosSearch = VideosSearch(query, limit = 20)
        channelList = {}
        youApi = YouApi()
        tasks = []        
        t1 = 0
        mongoCluster = pymongo.MongoClient("mongodb+srv://kaanakyuz:Skywalker1994!@vamblecluster.hc4nf.mongodb.net/")     
        db = mongoCluster["myFirstDatabase"]
        channelsDb = db["channels"].find()   
        
        
        while searchCounter != constants.SEARCH_LIMIT:
            t0 = time.time()
            videos = await youApi.videoSearch(videosSearch)
            t1 = time.time() - t0 + t1

            for video in videos:
                channelId = video['channel']["id"]
                if channelId not in channelList.keys():
                    channelList[channelId] = {"information": {}, "videos": []}
                    tasks.append(asyncio.create_task(youApi.addChannelInformation(channelList[channelId], channelId, channelsDb)))                   
                channelList[channelId]["videos"].append(Helper.parseVideoInformation(video))
            searchCounter = searchCounter + 1
        
        await asyncio.gather(*tasks)
        channelList["videoSearchTime"] = t1
                
        return channelList 
    
    def channelDetailsService(channelId: str, query: str):
        pass
    