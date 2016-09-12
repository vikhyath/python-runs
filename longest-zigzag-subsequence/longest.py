# does not work
# refer http://stackoverflow.com/questions/6914969/dynamic-programming-find-longest-subsequence-that-is-zig-zag


alist = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
alist = [1, 3, 5, 4, 2]
track = {}
parents = {}

for i, val in enumerate(alist):
	j = i - 1
	track[alist[i]] = {
		'count': 1,
		'last': None
	}
	while (j >= 0):
		if alist[i] > alist[j]:
			if alist[j] in track:
				if track[alist[j]]['last'] == 'dec' or not track[alist[j]]['last']:
					track[alist[i]]['last'] = 'inc'

					if track[alist[i]]['count'] < track[alist[j]]['count'] + 1:
						track[alist[i]]['count'] = track[alist[j]]['count'] + 1

				else:
					if track[alist[j]]['count'] + 1 > track[alist[i]]['count']:
						track[alist[j]]['last'] = 'inc'
						if track[alist[j]]['count'] < track[alist[j]]['count']:
							track[alist[j]]['count'] = track[alist[j]]['count']

		if alist[i] < alist[j]:		
			if alist[j] in track:
				if track[alist[j]]['last'] == 'inc' or not track[alist[j]]['last']:
					track[alist[i]]['last'] = 'dec'

					if track[alist[i]]['count'] < track[alist[j]]['count'] + 1:
						track[alist[i]]['count'] = track[alist[j]]['count'] + 1

				else:
					if track[alist[j]]['count'] + 1 > track[alist[i]]['count']:
						track[alist[i]]['last'] = 'dec'
						if track[alist[j]]['count'] < track[alist[j]]['count']:
							track[alist[j]]['count'] = track[alist[j]]['count']

		j -= 1

print(track)