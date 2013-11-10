# Given an unsorted array, find the max length of subsequence in which the numbers are in incremental order.
# Refer http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming

alist = [2, 6, 3, 4, 1, 2, 9, 5, 8]
sublist = []
parents = [None for x in xrange(0, len(alist))]
def main():
    for index, num in enumerate(alist):
        # If the length of the subsequence list is 0 or if the last number in the list is less than current, add current
        # because by doing this we are only increasing the length of the subsequence
        if len(sublist) == 0 or alist[sublist[len(sublist)-1]] < num:
            if len(sublist) > 0:
                parents[index] = sublist[-1]
            
            # Note that the element inserted last, will not have a child
            sublist.append(index)
            continue

        # If the last number is greater than or equal to current then replace the subsequence list with the current number, for a 
        # target that is >= current and is the least greatest element in the subsequence list
        if alist[sublist[len(sublist)-1]] >= num:
            replace(sublist, index)

    # The parents array stores the index position of the parent of the current index in the list
    #   hence we need to pop out the last element of the subsequence list and then start finding its parents until we hit None
    current_parent = sublist[-1]
    lis = []
    while current_parent is not None:
        lis.append(alist[current_parent])
        current_parent = parents[current_parent]
    lis.reverse()
    print lis


def replace(sublist, newindex):
    pos = binsearch(sublist, 0, len(sublist)-1, alist[newindex], None)
    sublist[pos] = newindex
    parents[newindex] = sublist[pos-1]

def binsearch(sublist, start, end, num, pos):
    if start >= end:
        if pos is None:
            return start
        else:
            if alist[sublist[start]] <= alist[sublist[pos]] and alist[sublist[start]] >= num:
                pos = start
            return pos

    target = (start + end)/2
    if alist[sublist[target]] < num:
        start = target + 1
    else:
        # Store the current greatest position
        pos = target
        end = target - 1
    return binsearch(sublist, start, end, num, pos)

if __name__ == '__main__':
    main()