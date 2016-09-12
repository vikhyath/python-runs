# Task schedule: given a sequence of task like 
# A B C (3 different tasks), and a coldtime, 
# which means you need to wait for that much time to start next [same] task. 

# Input: string, n 
# Output: the best task-finishing sequence. 

# eg. input: AAABBB, 2 
# Output: AB_AB_AB 
# ( "_" represents do nothing and wait)

#!/usr/bin/env python

def schedit(schedule, cool):
	scheduled = 0
	coolers = {}
	idx = 0
	order = ''
	schedule = list(schedule)
	while True:
		if scheduled == len(schedule):
			break

		idx = 0
		canSchedule = False
		while(idx < len(schedule)):

			if schedule[idx] != '_' and \
				(schedule[idx] not in coolers or coolers[schedule[idx]] <= 0):
				for item, val in coolers.items():
					coolers[item] -= 1

				order += schedule[idx]
				coolers[schedule[idx]] = cool
				schedule[idx] = '_'
				canSchedule = True

				scheduled += 1
				break

			idx += 1

		# silent period, could not schedule anything
		if not canSchedule:
			for item, val in coolers.items():
				coolers[item] -= 1
			order += '_'

	return order

print(schedit('AAABBB', 2))
print(schedit('AAAAAABBBBCCCDCCCCCCC', 2))