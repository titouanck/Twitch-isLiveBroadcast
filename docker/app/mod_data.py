# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mod_data.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchevrie <tchevrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/10 06:32:54 by tchevrie          #+#    #+#              #
#    Updated: 2024/01/10 09:27:55 by tchevrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json, sys

# **************************************************************************** #

def	get_data():
	filename = "./data.json"

	try:
		file_obj = open(filename, 'r')
	except Exception as e:
		raise e
	data = json.load(file_obj)
	needed_keys = ["twitch_channel_to_monitor", "twitch_channel_to_send_message", "messages_to_send", "cooldown_between_messages"]
	for key in needed_keys:
		if key not in data:
			raise Exception(f"Key '{key}' missing from JSON file.")

	expected_types = {
		"twitch_channel_to_monitor": str,
		"twitch_channel_to_send_message": str,
		"messages_to_send": list,
		"cooldown_between_messages": int
	}

	for key, expected_type in expected_types.items():
		if key in data and not isinstance(data[key], expected_type):
			raise ValueError(f"Value from key '{key}' is not of the expected type ({expected_type}).")

	if not (all(key in data for key in needed_keys) and all(isinstance(data[key], expected_types[key]) for key in expected_types)):
		raise Exception("The data is invalid.")

	get_data.channel_to_monitor 		= data["twitch_channel_to_monitor"]
	get_data.channel_to_send_message 	= data["twitch_channel_to_send_message"]
	get_data.messages_to_send 			= data["messages_to_send"]
	get_data.cooldown_between_messages 	= data["cooldown_between_messages"]

# **************************************************************************** #
