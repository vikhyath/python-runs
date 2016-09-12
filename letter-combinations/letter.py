# Given a digit string, return all possible letter combinations
#  that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) 
# is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer
#  could be in any order you want.

#!/usr/bin/env python

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#!/usr/bin/env python

def comb(digits):
	mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
	res = ['']

	for char in digits:
		digit = int(char)
		temp = []
		for elem in mapping[digit]:
			for result in res:
				temp.append(elem+result)

		res = temp

	return res

print(comb("23"))
