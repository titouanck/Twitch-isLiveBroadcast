# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_time.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchevrie <tchevrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 12:20:21 by titouanck         #+#    #+#              #
#    Updated: 2024/01/10 16:20:48 by tchevrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# **************************************************************************** #

def get_localtime():
    database_time = datetime.now(timezone.utc)
    utc = ZoneInfo('UTC')
    localtz = ZoneInfo("Europe/Paris")
    utctime = database_time.replace(tzinfo=utc)
    localtime = utctime.astimezone(localtz)
    return localtime

def get_date():
    localtime = get_localtime()
    date_format = "%Y-%m-%d"
    current_date = localtime.strftime(date_format)
    return current_date

def get_time():
    localtime = get_localtime()
    date_format = "%H:%M:%S"
    current_time = localtime.strftime(date_format)
    return current_time

if __name__ == "__main__":
    print(get_date())
    print(get_time())

# **************************************************************************** #
