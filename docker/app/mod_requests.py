# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_requests.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchevrie <tchevrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 14:10:00 by titouanck         #+#    #+#              #
#    Updated: 2024/01/11 04:30:06 by tchevrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os, requests, time

API_URL    = "https://api.twitch.tv/helix"
APP_ID     = os.environ["APP_ID"]
USER_TOKEN = os.environ["USER_TOKEN"]

# **************************************************************************** #

def get_response(endpoint, params, headers):
    return requests.get(API_URL + endpoint, params=params, headers=headers)

def post_response(endpoint, params, headers):
    return requests.post(API_URL + endpoint, params=params, headers=headers)

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
        is_live_broadcast.data = None
        raise Exception(f"is_live_broadcast(): Error: {response.status_code}, {response.text}")

def get_user_id(user_login):
    endpoint = "/users"
    params   = {'login': user_login}
    headers  = {"Authorization": f"Bearer {USER_TOKEN}", "Client-ID": APP_ID}
    
    get_user_id.id = None
    response = get_response(endpoint, params, headers)
    if response.status_code == 200:
        get_user_id.data = response.json()
        if bool(get_user_id.data.get("data")) and bool(get_user_id.data["data"][0].get("id")):
            get_user_id.id = get_user_id.data["data"][0]["id"]
    else:
        get_user_id.data = None
        raise Exception(f"get_user_id(): Error: {response.status_code}, {response.text}")
    return get_user_id.id

def create_clip(user_login):
    try:
        broadcaster_id = get_user_id(user_login)
    except Exception as e:
        raise e
    endpoint = "/clips"
    params   = {'broadcaster_id': broadcaster_id}
    headers  = {"Authorization": f"Bearer {USER_TOKEN}", "Client-ID": APP_ID}
    
    create_clip.clip_id = None
    response = post_response(endpoint, params, headers)
    if response.status_code == 202:
        create_clip.data = response.json()
        if bool(create_clip.data.get("data")) and bool(create_clip.data["data"][0].get("id")):
            create_clip.clip_id = create_clip.data["data"][0].get("id")
    else:
        create_clip.data = None
        raise Exception(f"create_clip(): Error: {response.status_code}, {response.text}")
    return create_clip.clip_id

def get_clip_url(clip_id):
    endpoint = "/clips"
    params   = {'id': clip_id}
    headers  = {"Authorization": f"Bearer {USER_TOKEN}", "Client-ID": APP_ID}

    get_clip_url.clip_url = None
    response = get_response(endpoint, params, headers)
    if response.status_code == 200:
        get_clip_url.data = response.json()
        if bool(get_clip_url.data.get("data")) and bool(get_clip_url.data["data"][0].get("thumbnail_url")):
            thumbnail = get_clip_url.data["data"][0].get("thumbnail_url")
            index = thumbnail.find('-preview')
            get_clip_url.clip_url = thumbnail[:index] + '.mp4'
    else:
        get_clip_url.data = None
        raise Exception(f"get_clip_url(): Error: {response.status_code}, {response.text}")
    return get_clip_url.clip_url

# **************************************************************************** #

def get_username():
    endpoint = "/users"
    params   = {}
    headers  = {"Authorization": f"Bearer {USER_TOKEN}", "Client-ID": APP_ID}
    
    get_username.login = None
    response = get_response(endpoint, params, headers)
    if response.status_code == 200:
        get_username.data = response.json()
        if bool(get_username.data.get("data")) and bool(get_username.data["data"][0].get("login")):
            get_username.login = get_username.data["data"][0]["login"]
    else:
        get_username.data = None
        raise Exception(f"get_username(): Error: {response.status_code}, {response.text}")
    return get_username.login

if __name__ == "__main__":
    clip_url = get_clip_url("WanderingSteamyGoshawkStinkyCheese-a0yfdzi5CRG74DYb")
    r = requests.get(clip_url)

    if r.headers['Content-Type'] == 'binary/octet-stream':
        
            f.write(r.content)

# **************************************************************************** #
