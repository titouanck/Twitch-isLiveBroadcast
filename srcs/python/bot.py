# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/05 12:08:23 by titouanck         #+#    #+#              #
#    Updated: 2024/01/05 20:36:57 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import requests
import threading
import asyncio
import os
import time

from twitchio.ext   import commands
from datetime       import datetime

# **************************************************************************** #

def main():
    twitchBot = Bot()
    twitchBot.run()

# **************************************************************************** #

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ['TOKEN'], prefix=os.environ['PREFIX'], initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        message = "bonjour"

        channelObj = self.get_channel(os.environ['CHANNEL'])
        if channelObj:
            while True:
                if isLiveBroadcast(os.environ['CHANNEL']):
                    writeToLogFile(os.environ['CHANNEL'] + " is currently live.")
                    while isLiveBroadcast(os.environ['CHANNEL']):
                        time.sleep(120)
                else:
                    writeToLogFile(os.environ['CHANNEL'] + " is offline.")
                    while True:
                        if isLiveBroadcast(os.environ['CHANNEL']):
                            writeToLogFile(os.environ['CHANNEL'] + " just went LIVE!")
                            await channelObj.send(message)
                            writeToLogFile("Closing the program.")
                            sys.exit(0)
                            return
                        else:
                            time.sleep(1)
                    
# **************************************************************************** #

def isLiveBroadcast(channel):
    url = "https://www.twitch.tv/"
    response = requests.get(url + channel)

    if response.ok and "isLiveBroadcast\":true" in response.text:
        return True
    else:
        return False

# **************************************************************************** #

def findFilename():
    date_format = "%Y-%m-%d"
    today_date = datetime.now().strftime(date_format)
    filename = f"/root/logs/{today_date}.log"
    return filename

def createLogFile():
    filename = findFilename()

    if os.path.isfile(filename):
        print(f"{filename} already exists")
        logFile = open(filename, 'a')
    else:
        print(f"{filename} has been created")
        logFile = open(filename, 'w')
    logFile.write("# **************************************** #\n")
    return logFile

def writeToLogFile(str):
    currentTime = datetime.now().strftime("%H:%M:%S")
    logFile.write(f"[{currentTime}] {str}\n")
    logFile.flush()
    print(str)

# **************************************************************************** #

logFile = createLogFile()

if __name__ == "__main__":
    main()
    logFile.close()