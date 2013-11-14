def main():
    # alist = [3, 2, 5, 1, 4, 7, 9, 6, 8]
    # alist = [10, 40, 1, 2, 5]
    alist = [10, 50, 49, 48, 11, 12]

    # i, j and k are three variables which will point to the sequence
    # tempi and tempj are temporary variables to point to inc. sequences
    #   which occur later on in the series, eg: 10, 40, 1, 2, 5. In this case
    #   i and j will have 10 and 40, tempi and tempj will be greedy to store lesser values but inc. sequence
    i = -1
    j = -1
    k = -1
    tempi = -1
    tempj = -1

    for num in alist:
        
        # for the first number seen
        if i == -1:
            i = num

        # try to get two numbers, but if second is less than first, store second in i
        elif j == -1:
            if num <= i:
                i = num
            else:
                j = num

        # if we have a third number which is greater than j
        #   OR if the number is greater than greedy j (tempj) which always stored value lesser than j
        elif num > j or (tempj != -1 and num >= tempj):
            j = tempj
            k = num

            # who knows, there might be a greedier i (tempi) too, eg: 10, 40, 1, 2, 5
            if tempi != -1:
                i = tempi

            # we found our three candidates, break loop
            break

        # greedy approach to store future inc sequences but lesser than current i and j in the hope that there will be a k
        #   that is lesser than i, j but greater than tempi and tempj
        elif num <= j:
            # if number is less than i and tempi is not init yet OR number is <= tempi, this is needed to ensure tempi
            #   will only store absolute minimum and not greedily take everything that is less than i
            if num <= i and (tempi == -1 or num <= tempi):
                tempi = num
            else:
                tempj = num 

    if i != -1 and j != -1 and k != -1:
        print i,j,k
    else:
        print 'no such sequence exists'
if __name__ == '__main__':
    main()