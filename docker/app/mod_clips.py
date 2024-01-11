# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_clips.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchevrie <tchevrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/11 04:01:15 by tchevrie          #+#    #+#              #
#    Updated: 2024/01/11 12:12:35 by tchevrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time, requests
from mod_requests	import create_clip, get_clip_url
from mod_files      import open_clip, write_logs

# **************************************************************************** #

def get_clip(channel):
    try:
        time.sleep(21)
        clip_id = create_clip(channel)
        time.sleep(5)
        clip_url = get_clip_url(clip_id)
        r = requests.get(clip_url)
        if r.headers['Content-Type'] == 'binary/octet-stream':
            file_obj = open_clip(channel)
            file_obj.write(r.content)
        else:
            write_logs(f"Failed to download clip from: id={clip_id}&url={clip_url}")
    except Exception as e:
        write_logs(e)
