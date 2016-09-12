#!/usr/bin/env python

alist = ['5-7', '7-11', '14-18', '12-16', '30-40', '2-8']

alist = sorted(alist, key=lambda x:int(x.split('-')[0]))

merged = []

print(alist)
for ele in alist:
	if not len(merged):
		merged.append(ele)
		continue

	top = merged.pop().split('-')
	start = int(top[0])
	end = int(top[1])

	ele = ele.split('-')
	x = int(ele[0])
	y = int(ele[1])

	if x <= end or end + 1 == x:
		if y <= end:
			# nothing to, whole consume
			# 1-8, 6-7 or 1-8, 6-8
			pass

		else:
			end = y

		merged.append(str(start) + '-' + str(end))

	else:
		merged.append(str(start) + '-' + str(end))
		merged.append(str(x) + '-' + str(y))

print(merged)

