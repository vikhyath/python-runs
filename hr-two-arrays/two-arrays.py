import sys

# failed twice because conversion to int after .split() was not happening, hence i used map

def newcheck(aline, bline, least):
    for num in aline:
        num = int(num)
        diff = int(least) - num
        if diff < 0:
            continue
        index = None
        for x in bline:
            if int(x) >= diff:
                index = bline.index(x)
        if index is not None:
            del bline[index]
        else:
            print 'NO'
            return
    print 'YES'

count = int(sys.stdin.readline())
while count > 0:
    count -= 1
    setuplist = sys.stdin.readline().strip().split()
    aline = map(int, sys.stdin.readline().strip().split())
    bline = map(int, sys.stdin.readline().strip().split())
    aline = sorted(aline)
    bline = sorted(bline)
    newcheck(aline, bline, setuplist[1])