# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_files.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 12:45:06 by titouanck         #+#    #+#              #
#    Updated: 2024/01/08 07:16:43 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from mod_time import get_date, get_time

PATH_DIRECTORY = "./channels"
LOGS_DIRECTORY = "logs"
CHAT_DIRECTORY = "chat"
TWITCH_CHANNEL = os.environ["TWITCH_CHANNEL"].lower()

# **************************************************************************** #

def open_file(filename):
    if os.path.isfile(filename):
        file_obj = open(filename, 'a')
        file_obj.write("# **************************************** #\n")
        file_obj.write(f"[{get_time()}] \"{filename}\" already exists\n")
        file_obj.flush()
    else:
        file_obj = open(filename, 'w')
        os.chmod(filename, 0o766)
        file_obj.write(f"[{get_time()}] \"{filename}\" has been created\n")
        file_obj.flush()
    return file_obj

# **************************************************************************** #

def open_logs(twitch_channel):
    parent_directory = PATH_DIRECTORY + '/' + twitch_channel + '/' + LOGS_DIRECTORY
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    os.chmod(parent_directory, 0o777)
    os.chmod(parent_directory.rstrip('/' + LOGS_DIRECTORY), 0o777)

    open_logs.date     = get_date()
    open_logs.filename = parent_directory + '/' + open_logs.date + ".log"
    open_logs.file_obj = open_file(open_logs.filename)
    return open_logs.file_obj

def open_chat(twitch_channel):
    parent_directory = PATH_DIRECTORY + '/' + twitch_channel + '/' + CHAT_DIRECTORY
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    os.chmod(parent_directory, 0o777)
    os.chmod(parent_directory.rstrip('/' + CHAT_DIRECTORY), 0o777)

    open_chat.date     = get_date()
    open_chat.filename = parent_directory + '/' + open_chat.date + ".log"
    open_chat.file_obj = open_file(open_chat.filename)
    return open_chat.file_obj

# **************************************************************************** #

def write_logs(str):
    if open_logs.date != get_date():
        open_logs.file_obj.close()
        open_logs(TWITCH_CHANNEL)
    str = f"[{get_time()}] {str}"
    open_logs.file_obj.write(str + "\n")
    open_logs.file_obj.flush()
    print(str)

def write_chat(str):
    if open_chat.date != get_date():
        open_chat.file_obj.close()
        open_chat()
    str = f"[{get_time()}] {str}"
    open_chat.file_obj.write(str + "\n")
    open_chat.file_obj.flush()
    print(str)

# **************************************************************************** #
