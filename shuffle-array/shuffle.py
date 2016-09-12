# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. 
# Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import random

class Solution:
	def __init__(self, nums):
		self.nums = nums
		self.randnums = nums.copy()

	def shuffle(self):
		for idx in range(len(self.nums)):
			# can also do randrange(idx+1) -> point in both cases is to have a
			# a chance to return the original array
			randidx = random.randrange(idx, len(self.nums))


			# swap idx and randidx
			temp = self.randnums[idx]
			self.randnums[idx] = self.randnums[randidx]
			self.randnums[randidx] = temp

		return self.randnums

	def reset(self):
		self.randnums = self.nums

sol = Solution([1, 2, 3, 4, 5, 6])

sol.shuffle()
print(sol.randnums)

sol.shuffle()
print(sol.randnums)

sol.reset()
print(sol.randnums)
