def count(nums):

	target = 2
	if len(nums) < 3:
		return False

	res = 0
	for idx in range(0, len(nums) - 2):
		j = idx + 1

		k = len(nums) - 1

		while(j < k):
			if nums[idx] + nums[j] + nums[k] < target:
				res += k - j
				j += 1
			else:
				k -= 1

	return res

print(count([-2, 0, 1, 3]))
print(count([-2, 0]))
print(count([-6, -2, 0, 1, 3, 7]))
