import asyncio
from youtubesearchpython.__future__ import *
from helpers.decorators import PerformaceTester, AsyncErrorHandler
from helpers.helper import Helper
import helpers.constants as constants
import googleapiclient.discovery

class YouApi:
    
    def __init__(self):
        self.youtube = googleapiclient.discovery.build(
            constants.API_SERVICE_NAME, constants.API_VERSION, developerKey = constants.DEVELOPER_KEY)
    
  
    @AsyncErrorHandler
    async def addChannelInformation(self, channel, channelId, channelsDb):
        
        for x in channelsDb:
            if x["channelId"] ==  channelId:
                del x["_id"]
                channel["information"] = x
                return
        
        request = self.youtube.channels().list(
            id= channelId,
            part="snippet,statistics,contentDetails"
        )
        
        channel["information"] = Helper.parseChannelInformation(request.execute())
        return 
    
            
    @AsyncErrorHandler    
    async def addVideoInformation(self, channel, videoId: str):
        
        response = await Video.getInfo(videoId)
        
        if Helper.isVideoFiltered(response):
            return
        
        channel["videos"] = Helper.parseVideoInformation(response)
        return
              
    @AsyncErrorHandler 
    async def videoSearch(self, videosSearch: VideosSearch):
           
        response =  await videosSearch.next()
        return response["result"]


    async def playlistInformation(self, channelId: str):
        tasks = []
        playlist = Playlist(playlist_from_channel_id(channelId))
        
        await playlist.getNextVideos()
        videos = playlist.videos

        for video in videos:
            tasks.append(self.videoInformation(video["id"]))
        
        response = await asyncio.gather(*tasks)
        
        return response