

def main():
    alist = [1, 2, 4, 7, 11, 15]
    start = 0
    end = len(alist) - 1
    num = 28
    while (1):
        if start >= end:
            print 'no such numbers found'
            break
        asum = alist[start] + alist[end]
        if asum == num:
            print 'the two numbers are: %d and %d'%(alist[start], alist[end])
            break
        if asum > num:
            end -= 1
        else:
            start += 1

if __name__ == '__main__':
    main()