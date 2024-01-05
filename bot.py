# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/05 12:08:23 by titouanck         #+#    #+#              #
#    Updated: 2024/01/05 16:13:04 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import requests
import threading
import asyncio
import os

from time           import sleep
from twitchio.ext   import commands
from dotenv         import load_dotenv

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
                    while isLiveBroadcast(os.environ['CHANNEL']):
                        print(os.environ['CHANNEL'] + " was already live when the program started")
                        sleep(120)
                else:
                    while True:
                        if isLiveBroadcast(os.environ['CHANNEL']):
                            print(os.environ['CHANNEL'] + " is LIVE!")
                            await channelObj.send(message)
                            return
                        else:
                            print(os.environ['CHANNEL'] + " is offline.")
                            sleep(1)
                    
# **************************************************************************** #

load_dotenv()

def main():
    twitchBot = Bot()
    twitchBot.run()

# **************************************************************************** #

def isLiveBroadcast(channel):
    url = "https://www.twitch.tv/"
    response = requests.get(url + channel)

    if response.ok and "isLiveBroadcast\":true" in response.text:
        return True
    else:
        return False

# **************************************************************************** #

if __name__ == "__main__":
    main()
