import sys

difference = ''
count = 0
adict = {}
# failed 3 times because i missed an explicit int coversion while storing in hash, thanks Python! :'( :'(
# read the first line, grab the difference
# different approaches possible
# 1 for each number in list, check if its corresponding pair exists in list O(n^2)
# 2 to make this faster but at the cost of extra memory we can use a dictionary O(n)
# 3 we can also sort the input elements O(n) or O(n log n), depending on the input. then 
    # in a single for loop iteration, we can check if a corresponding pair exists O(n)
    # without extra space
for line in sys.stdin:
    alist = line.split()
    if difference is '':
        difference = alist[1]
        continue
    for number in alist:
        adict[int(number)] = 1
    for number in alist:
        expected = int(number) + int(difference)
        if expected in adict:
            count += 1
print count