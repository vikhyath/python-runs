
import math

alist = [2, 6, 3, 4, 1, 2, 9, 5, 8]

aset = []
parents = {}

def bin_search(aset, num, low=0, high=len(alist) - 1, pos=0):
	if len(aset) == 0:
		return False

	if low > high:
		return pos

	mid = math.floor((low + high)/2)

	if alist[aset[mid]] > num:
		pos = mid
		high = mid - 1
		return bin_search(aset, num, low, high, pos)

	elif alist[aset[mid]] < num:
		low = mid + 1
		pos = mid + 1
		return bin_search(aset, num, low, high, pos)

	elif alist[aset[mid]] == num:
		return False

for idx, val in enumerate(alist):
	if len(aset) == 0 or val > alist[aset[len(aset) - 1]]:
		if len(aset) == 0:
			parents[idx] = None
		else:
			parents[idx] = aset[-1]
		aset.append(idx)
	else:
		sub_idx = bin_search(aset, val, 0, len(aset) - 1)
		aset[sub_idx] = idx
		if sub_idx > 0:
			# pass
			parents[idx] = aset[sub_idx - 1]
	print(parents)

	print(aset)

print(parents)
