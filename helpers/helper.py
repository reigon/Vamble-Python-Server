

class Helper:
    
    def parseVideoInformation(video: str):
        viewCount = Helper.getValue(video, "viewCount")
        text = Helper.getValue(viewCount, "text")
        imageLink = Helper.getValue(video, "thumbnails")
        link = Helper.getValue(video, "link")
        publishedTime = Helper.getValue(video, "publishedTime")
        duration = Helper.getValue(video, "duration")
        
        return {"title" : video["title"],

                "viewCount" : text,
                # "keywords" : video["keywords"],
                "imageLink" : imageLink[-1]["url"],
                "link" : link,
                "publishedTime" : publishedTime, 
                "duration" : duration}
        
    
    def parseChannelInformation(channel: str):
        item = channel["items"][0]
        
        snippet = item["snippet"]
        title = Helper.getValue(snippet, "title")
        description = Helper.getValue(snippet, "description")
        country = Helper.getValue(snippet, "country")
        
        statistics = item["statistics"]
        viewCount = Helper.getValue(statistics, "viewCount")
        subscriberCount = Helper.getValue(statistics, "subscriberCount")
        videoCount = Helper.getValue(statistics, "videoCount")
        
        return  {"title" : title,
                 "description" : description,
                 "country" : country,
                 "viewCount" : viewCount,
                 "subscriberCount" : subscriberCount,
                 "videoCount" : videoCount}
        

    def isVideoFiltered(receivedVideo):
        if "123 GO" in receivedVideo["channel"]["name"] or "T-Series" in receivedVideo["channel"]["name"]: 
            return True
        elif "nursery rhymes" in receivedVideo["title"].lower() or "kids" in receivedVideo["title"].lower():
            return True
        else:
            return False
        
        
    def mapper(values, function): 
        mappedList = []
        for value in values:
            mappedList.append(function(value))
        return mappedList
    
    
    def getValue(dictionary, key):
        if key in dictionary.keys():
            return dictionary[key]