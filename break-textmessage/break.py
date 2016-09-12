# Given a character limit and a message, split 
# the message up into annotated chunks without cutting words as, 
# for example when sending the SMS 
# "Hi Sivasrinivas, your Uber is arriving now!" 
# with char limit 25, you should get 
# ["Hi Sivasrinivas,(1/3)", "your Uber is arriving(2/3)", "now!(3/3)"]

import math
def breakMe(message, limit):
	if len(message) <= limit:
		return message

	splits = int(math.ceil(len(message) / limit))

	if splits >= 10 and splits <= 99:
		buff = 7 # ( ) idx denom /
	else:
		buff = 5 # ( ) idx demon /

	splits = int(math.ceil((len(message) + splits*buff) / limit))

	start = buff
	pos = 0
	msg = []
	msgs = []

	# this works, another way to use while loop is show below
	
	# while start < limit and pos < len(message):
	# 	msg += message[pos]

	# 	pos += 1
	# 	start += 1

	# 	if start == limit or pos == len(message):
	# 		if pos < len(message)-1 and message[pos] != ' ':
	# 			# go back until whitespace
	# 			while (message[pos] != ' '):
	# 				pos -= 1
	# 				msg.pop()

	# 		start = buff
	# 		msgs.append(''.join(msg) + '(' + str(len(msgs) + 1) + '/' + str(splits) + ')')
	# 		msg = []

	# 		if pos < len(message) - 1 and message[pos] == ' ':
	# 			pos += 1
	# 			start -= 1

	while True:
		if pos == len(message):
			break

		while start < limit and pos < len(message):
			msg += message[pos]
			pos += 1
			start += 1

		if pos < len(message) - 1 and message[pos] != ' ':
			# pos needs to be moved to no space zone
			while message[pos] != ' ':
				pos -= 1
				msg.pop()

		start = buff
		msgs.append(''.join(msg) + '(' + str(len(msgs) + 1) + '/' + str(splits) + ')')
		msg = []

		if pos < len(message) and message[pos] == ' ':
			pos += 1
			start -= 1

	return msgs

print(breakMe("Hi Sivasrinivas, your Uber is arriving now!", 25))