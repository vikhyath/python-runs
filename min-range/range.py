# Given a set of ranges: 
# (e.g. 
#	S = {(1, 4), (30, 40), (20, 91) ,(8, 10), (6, 7), (3, 9), (9, 12), (11, 14)}.

# And given a target range R (e.g. R = (3, 13) - meaning the range 
# going from 3 to 13). Write an algorithm to find the smallest 
# set of ranges that covers your target range. All of the ranges in 
# the set must overlap in order to be considered as spanning the entire 
# target range. 

# (In this example, the answer would be {(3, 9), (9, 12), (11, 14)}.

def tellme(S, target):
	x = sorted(S, key=lambda x: x[0])

	start = target[0]
	end = target[1]
	suitable = []

	for ranger in x:
		# invalid target
		if ranger[1] < start:
			continue

		if len(suitable):
			latest = suitable.pop()
		else:
			latest = ranger

		if ranger[0] <= start:
			canPick = False
			if len(suitable):
				top = suitable[len(suitable)-1]
				if ranger[0] <= top[1] or ranger[0] == top[1] + 1:
					canPick = True

			if ranger[1] > latest[1] and ((ranger[0] <= start and ranger[0] <= target[0]) or canPick):		
				suitable.append(ranger)
			else:
				if ranger != latest:
					suitable.append(latest)
				suitable.append(ranger)

			if ranger[1] >= end:
				break

			start = ranger[1]

	print(suitable)

S = {(1, 4), (30, 40), (20, 91) ,(8, 10), (6, 7), (3, 9), (9, 12), (11, 14)}
target = (3, 13)

tellme(S, target)

S = {(1, 4), (3, 9), (5, 14), (6, 17), (17, 18)}
target = (6, 18)

tellme(S, target)

S = {(1, 4), (1, 5), (2, 9), (6, 17), (17, 18)}
target = (4, 18)

tellme(S, target)

S = {(3, 12), (8, 10), (9, 14), (10,15)}
target = (3, 15)

tellme(S, target)