# Given an array of positive integers (excluding zero) 
# and a target number. Detect whether there is a set 
# of consecutive elements in the array that add up to the target. 

# Example: a = {1, 3, 5, 7, 9} 
# target = 8 

# output = true ({3, 5}) 

# or target = 15 
# output = true : {3, 5, 7} 

# but if target = 6, output would be false. 
# since 1 and 5 are not next to each other.

a = [1, 7, 5, 3, 9]
target = 15

start = 0
end = 0 
summer = a[start]

# while True:
# 	summer += a[end]
# 	if summer < target:
# 		end += 1

# 	elif summer > target:
# 		summer -= a[start]
# 		start += 1
# 		summer -= a[end]

# 	elif summer == target:
# 		print(a[start:end+1])
# 		break

# 	if end == len(a) or start > end:
# 		print (None)
# 		break

if summer == target:
	print(a[start:start+1])

while end < len(a):
	if summer > target:
		summer -= a[start]
		start += 1
	else:
		end += 1
		if end < len(a):
			summer += a[end]

	if summer == target:
		print(a[start:end+1])
		break

