# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_irc.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 16:41:32 by titouanck         #+#    #+#              #
#    Updated: 2024/01/08 15:36:40 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket, time, os, select
from mod_files      import write_chat

TWITCH_CHANNEL  = os.environ["TWITCH_CHANNEL"].lower()
TWITCH_USERNAME = os.environ["TWITCH_USERNAME"].lower()
USER_TOKEN      = os.environ["USER_TOKEN"]

# **************************************************************************** #

def parse_irc_message(irc_message):
    messages     = ["NOTICE", "PART", "PING", "PRIVMSG"]
    index        = None
    message_type = None
    
    for some_message in messages:
        if some_message in irc_message:
            length = len(irc_message.split(some_message)[0])
            if index is None or length < index:
                message_type = some_message
                index = length
    if message_type == "PING":
        content = irc_message.split("PING :")[1]
    elif message_type == "PRIVMSG":
        username = irc_message[1:].split("!")[0]
        content = f"{username}: " + irc_message.split(f"PRIVMSG #{TWITCH_CHANNEL} :")[1]
    else:
        content = irc_message
    return message_type, content

# **************************************************************************** #

class IrcServer:

    def __init__(self):
        self.socket = None
    
    def send_data(self, command):
        self.socket.send((command + '\n').encode("UTF-8"))
    
    def send_privmsg(self, message):
        self.socket.send(f"PRIVMSG #{TWITCH_CHANNEL} :{message}\n".encode("UTF-8"))
        write_chat(f">> {TWITCH_USERNAME}: {message}")

    def send_pong(self, message):
        r = self.socket.send(f"PONG :{message}\n".encode("UTF-8"))
        write_chat(f">> /PONG {message}")
        return r

    def get_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect(("irc.chat.twitch.tv", 6667))

        self.send_data(f"PASS oauth:{USER_TOKEN}")
        self.send_data(f"NICK {TWITCH_USERNAME}")
        self.send_data(f"JOIN #{TWITCH_CHANNEL}")

    def listener(self):
        while True:
            try:
                response = self.socket.recv(1024).decode("utf-8")
                while "\n" in response:
                    splited_response = response.split("\n", 1)
                    response = splited_response[1]
                    message_type, content = parse_irc_message(splited_response[0])
                    if message_type == "PRIVMSG":
                        write_chat(f"<< {content}")
                    else:
                        if message_type != None:
                            write_chat(f"<< /{message_type} {content}")
                        else:
                            write_chat(f"<< {content}")
                        if message_type == "PING":
                            self.send_pong(content)
            except OSError as e:
                self.connect()

# **************************************************************************** #
