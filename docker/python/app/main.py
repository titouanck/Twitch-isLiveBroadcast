# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 13:26:34 by titouanck         #+#    #+#              #
#    Updated: 2024/01/08 15:23:31 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time, os, random, threading
from mod_files      import open_logs, open_chat, write_logs, write_chat
from mod_requests   import is_live_broadcast
from mod_irc        import IrcServer

TWITCH_CHANNEL  = os.environ["TWITCH_CHANNEL"].lower()
MESSAGE_TO_SEND = os.environ["MESSAGE_TO_SEND"]

# **************************************************************************** #

def main():
    open_logs(TWITCH_CHANNEL)
    open_chat(TWITCH_CHANNEL)
    main.irc_server = IrcServer()
    main.irc_server.get_socket()
    main.irc_server.connect()
    chat_thread = threading.Thread(target=main.irc_server.listener)
    chat_thread.start()
    routine()
    chat_thread.join()

# **************************************************************************** #

def routine():
    while True:
        if is_live_broadcast(TWITCH_CHANNEL):
            is_online()
        else:
            is_offline()

def is_online():
    title        = is_live_broadcast.data['data'][0]['title']
    game_name    = is_live_broadcast.data['data'][0]['game_name']
    viewer_count = is_live_broadcast.data['data'][0]['viewer_count']
    write_logs(TWITCH_CHANNEL + " is currently live streaming.")
    write_logs(f"{TWITCH_CHANNEL} {{game_name:'{game_name}', viewer_count:'{viewer_count}', title:'{title}'}}")
    time.sleep(300)

def is_offline():
    index = 0
    prefix = [" podaBRASGAUCHE", " podaBRASDROIT", " snayzyHELLO", " !", ""]
    message = MESSAGE_TO_SEND + random.choice(prefix)
    while not is_live_broadcast(TWITCH_CHANNEL):
        if index % 10 == 0:
            write_logs(f"{TWITCH_CHANNEL} is currently offline.")
        time.sleep(0.2)
        index += 1
    main.irc_server.send_privmsg(message)
    write_logs(TWITCH_CHANNEL + " just went LIVE!")
    time.sleep(300)

# **************************************************************************** #

if __name__ == "__main__":
    main()

# **************************************************************************** #
