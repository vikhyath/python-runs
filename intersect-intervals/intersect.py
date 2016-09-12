# Given a set of non-overlapping intervals, insert a new 
# interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted 
# according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and 
# merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with 
# [3,5],[6,7],[8,10].

#!/usr/bin/env python

def insert(intervals, new):
	# find suitable start
	alist = []
	sofar = -1
	for idx, inter in enumerate(intervals):
		if new[0] > inter[1]:
			alist.append(inter)
			sofar = idx
		else:
			break

	# now insert new
	minstart = new[0]
	maxend = new[1]
	for idx in range(sofar+1, len(intervals)):
		if intervals[idx][0] > maxend:
			break
		minstart = min(intervals[idx][0], minstart)
		maxend = max(intervals[idx][1], maxend)
		sofar = idx

	alist.append([minstart, maxend])

	for idx in range(sofar+1, len(intervals)):
		alist.append(intervals[idx])

	print(alist)

insert([[1,3], [6,9]], [2,5])
insert([[1, 3], [6, 9]], [2, 7])
insert([[1, 3], [6, 9]], [4, 5])
insert([[3, 5], [6, 9]], [1, 2])
insert([[3, 5], [6, 9]], [10, 12])

