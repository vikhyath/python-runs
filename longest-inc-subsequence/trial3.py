arr = [1, 2, 6, 3, 14, 7, 10, 9, 0, 12]

dp = [1] * len(arr)

index = 1
while (index < len(arr)):
	subindex = index - 1
	while (subindex >= 0):
		if arr[index] > arr[subindex]:
			dp[index] = max(dp[index], 1 + dp[subindex])
		subindex -= 1
	index += 1

print(dp)
print(dp[len(arr) - 1])