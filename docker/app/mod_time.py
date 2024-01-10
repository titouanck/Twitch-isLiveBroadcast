# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_time.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: titouanck <chevrier.titouan@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/06 12:20:21 by titouanck         #+#    #+#              #
#    Updated: 2024/01/06 12:44:42 by titouanck        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from zoneinfo import ZoneInfo

# **************************************************************************** #

def get_localtime():
    database_time = datetime.utcnow()
    utc = ZoneInfo('UTC')
    localtz = ZoneInfo('localtime')
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

# **************************************************************************** #
