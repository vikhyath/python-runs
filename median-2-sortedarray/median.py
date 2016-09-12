# here are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

# https://discuss.leetcode.com/topic/22406/python-o-log-min-m-n-solution/2

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

#!/usr/bin/env python

def __findMedian(a, b, k):
	if len(a) > len(b):
		a,b = b,a

	k = int(k)
	if not len(a):
		return b[k]


	if k == len(a) + len(b) - 1:
		return max(a[-1], b[-1])

	i = int(len(a)/2)
	j = k - i

	if a[i] > b[j]:
		return __findMedian(a[:i], b[j:], i)
	else:
		return __findMedian(a[i:], b[:j], j)


def median(a, b):
	length = len(a) + len(b)

	return __findMedian(a, b, length / 2) if length % 2 == 1 \
		else (__findMedian(a, b, (length / 2) - 1 ) + __findMedian(a, b, length / 2)) / 2

print(median([2, 10, 20], [3, 5, 16, 40, 48, 50]))

