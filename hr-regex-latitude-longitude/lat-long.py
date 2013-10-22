# Determine valid latitude/longitude pairs. Given a line of text which possibly contains the latitude and longitude of a point,
# can you use regular expressions to identify the latitude and longitude referred to.

import sys, re

def process(numlist):
    sign = 1
    if numlist[0] == '-':
        sign = -1
    if numlist[0] == '-' or numlist[0] == '+':
        del numlist[0]
    
    # case when string starts with 0 but does not have a decimal right after it
    if numlist[0] == '0' and numlist[1] != '.':
        return None
    return sign * float(''.join(numlist))

def checkvalid(lat, lng):
    if lat >= -90 and lat <= 90 and lng >= -180 and lng <= 180:
        return 'Valid'
    else:
        return 'Invalid'

count = int(sys.stdin.readline().strip())
while count > 0:
    line = sys.stdin.readline().rstrip()
    numregex = '[-+]?[0-9]{0,3}(?:(?:\.[0-9]+)|(?:[0-9]+))'
    pattern = '(' + numregex + ',\s{1}' + numregex + ')'
    regex1 = re.compile(pattern)
    regex2 = re.compile(numregex)
    search = regex1.findall(line)
    if len(search) > 0:
        # found something, try extracting numbers
        latlong = regex2.findall(search[0])
        
        # form list because easier to check for +/- in 0th index and delete later
        latlist = list(latlong[0])
        longlist = list(latlong[1])
        
        # get floats back
        lat = process(latlist)
        lng = process(longlist)
        
        if lat is None or long is None:
            print 'Invalid'
            count -= 1
            continue
        
        print checkvalid(lat, lng)
        # print latlong
    else:
        print 'Invalid'
    count -= 1