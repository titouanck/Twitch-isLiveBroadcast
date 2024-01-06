# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_requests.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 14:10:00 by titouanck         #+#    #+#              #
#    Updated: 2024/01/06 22:00:47 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os, requests
from mod_files import write_logs, write_chat

API_URL    = "https://api.twitch.tv/helix"
APP_ID     = os.environ["APP_ID"]
USER_TOKEN = os.environ["USER_TOKEN"]

# **************************************************************************** #

def get_response(endpoint, params, headers):
    return requests.get(API_URL + endpoint, params=params, headers=headers)

# **************************************************************************** #

def is_live_broadcast(user_login):
    endpoint = "/streams"
    params   = {'user_login': user_login}
    headers  = {"Authorization": f"Bearer {USER_TOKEN}", "Client-ID": APP_ID}
    
    response = get_response(endpoint, params, headers)
    if response.status_code == 200:
        is_live_broadcast.data = response.json()
        is_live = bool(is_live_broadcast.data.get('data'))
        if is_live:
            return True
        else:
            return False
    else:
        write_logs(f"is_live_broadcast(): Error: {response.status_code}, {response.text}")
        sys.exit(1)

# **************************************************************************** #
