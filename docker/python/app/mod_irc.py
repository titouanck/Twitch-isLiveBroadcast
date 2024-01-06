# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_irc.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 16:41:32 by titouanck         #+#    #+#              #
#    Updated: 2024/01/06 22:01:03 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, time, os

TWITCH_CHANNEL  = os.environ["TWITCH_CHANNEL"]
TWITCH_USERNAME = os.environ["TWITCH_USERNAME"]
USER_TOKEN      = os.environ["USER_TOKEN"]

# **************************************************************************** #

class IrcServer:

    def __init__(self):
        self.socket = None
    
    def send_data(self, command):
        self.socket.send((command + '\n').encode("UTF-8"))
    
    def send_message(self, message):
        self.socket.send(f"PRIVMSG #{TWITCH_CHANNEL} :{message}\n".encode("UTF-8"))

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("irc.chat.twitch.tv", 6667))

        self.send_data(f"PASS oauth:{USER_TOKEN}")
        self.send_data(f"NICK {TWITCH_USERNAME}")
        self.send_data(f"JOIN #{TWITCH_CHANNEL}")

# **************************************************************************** #
