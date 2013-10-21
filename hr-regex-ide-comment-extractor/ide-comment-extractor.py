 # write a program, which accepts as input, a C or C++ or Java program and outputs only the comments from those programs.

import sys, re
regex1 = re.compile('/\*.*')
regex2 = re.compile('.*\*/')
regex3 = re.compile('//.*')
previousopen = 0

while 1:
    line = sys.stdin.readline()
    if not line:
        break
    line.strip()
    match1 = regex1.findall(line)
    match2 = regex2.findall(line)
    match3 = regex3.findall(line)
    matchlist = []
    
    # /* matching
    if len(match1) > 0:
        matchlist = match1
        # check if line also matches closing */
        if len(match2) > 0:
            pass
        else:
            previousopen = 1
    # a previous opening multi line comment was found and now its closing pair, so this should stop recording lines
    elif len(match2) > 0 and previousopen == 1:
        previousopen = 0
        matchlist = match2
    # // match
    elif len(match3) > 0:
        matchlist = match3
    # plain text line, print because it previously had an open /*
    elif previousopen == 1:
        if len(line) > 0:
            matchlist = list(line)
    if len(matchlist) > 0:
        print ''.join(matchlist).rstrip()