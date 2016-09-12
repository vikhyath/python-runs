# Given predicted stock prices for next n days for a stock 
# e.g : 10, 30, 42, 15, 20, 50, 10, 25 find the maximum profit 
# that can be made with a single buy-sell transaction. 
# If no profit can be made return 0. In the example buying at 15 
# and selling at 50 gives maximum profit. Note that the two 
# prices are neither minimum nor maximum in the array.

arr = [10, 30, 42, 15, 20, 50, 10, 25]
arr = [15, 60, 10, 45]
arr = [10, 45, 15, 50]

buy = None
sell = None
bestprice = None
newbuy = None

for idx, price in enumerate(arr):
	if newbuy is None or price < arr[newbuy]:
		newbuy = idx
		continue

	if bestprice is None or price - arr[newbuy] > bestprice:
		bestprice = price - arr[newbuy]
		sell = idx
		buy = newbuy

print(buy)
print(sell)
print(bestprice)

