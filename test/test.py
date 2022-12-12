

from youtubesearchpython.__future__ import *
import asyncio

from api.youapi import YouApi



youApi = YouApi()

# print(asyncio.run(youApi.playlistInformation
#                   (channelId= "UCv2LNRhF34_v1VNC08ZuooA")))

# print(type(youApi.videoInformation("IUPJsK8fJBQ")))


async def asyncFunc(x):
    
    await asyncio.sleep(x)
    return x


async def main():
    tasks = {}
    tasks["kaan"] = []
    for x in range(10):
        tasks["kaan"].append(asyncio.create_task(asyncFunc(x)))
    await asyncio.sleep(3)
    
    print(tasks["kaan"][1].result())
    
asyncio.run(main())

