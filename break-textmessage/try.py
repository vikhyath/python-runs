# Given a message "one two three four five six seven eight nine",
#  chop it in chunks(no exceed the give buffer size) and print
#   out to the screen. Need to maintain the word and do not chop it off.
# I.E.: buffer size is 15
# one two three (1/4)
# four five six (2/4)
# seven eight (3/4)
# nine (4/4)  

#!/usr/bin/env python

string = "one two three four five six seven eight nine"
string = "Hi Sivasrinivas, your Uber is arriving now!"
buf = 15

start = 0
end = 0
splits = []
count = 1
while end < len(string):
	distance = end-start+1
	if distance == buf or end + 1 == len(string):

		# check for space
		if (end + 1 < len(string) and string[end + 1] == ' ') \
		 or (end+1 == len(string)):
		 	splits.append(string[start:end+1])
		else:
			# else back track until a previous space
			while string[end] != ' ':
				end -= 1
			splits.append(string[start:end])

		start = end + 1

	end += 1

print(splits)