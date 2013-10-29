alist =             [1, 2, 4, 5, 6, 7]
blist =          [9, 9, 3, 3, 2, 1, 9]
sumlist = []

alen = len(alist) - 1
blen = len(blist) - 1

carry = 0
while alen >= 0 or blen >= 0:
    a = 0
    b = 0
    if alen >= 0:
        a = alist[alen]
    if blen >= 0:
        b = blist[blen]
    absum = (a + b + carry) % 10
    carry = (a + b + carry) / 10
    sumlist[:0] = [absum]
    alen -= 1
    blen -= 1

if carry > 0:
    sumlist[:0] = [carry]
print sumlist