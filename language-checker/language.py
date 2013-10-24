# Language validity
# In a language, there are only 4 characters h, i, r, e. and we have to write a function which takes a string as input and returns whether the given input string is a valid-word or not. 

# Definition of valid word : 
# 1. A given word is a valid word if it is of the form h^n i^n r^n e^n where n >=1. (eg: hhiirree) 
# 2. Valid words has concatenation property i.e. if w1 and w2 are valid words w1w2 is also a valid word.

# Runs in constant memory space, the check terminates ones it determines that an alien character not present in our language definition is found
# Runs in O(n) time
chars = ['h', 'i', 'r', 'e']

def check(string, adict = None):
    if adict is None:
        adict = {}
    count = 0
    previous = None
    wordcomplete = 0   
    for letter in string:
        if letter not in chars:
            print 'Invalid for:',string
            return

        # first word, that is not a part of concatenated sequence, ignore checks
        if letter == 'h' and wordcomplete == 0:
            pass

        # found last valid letter, now make the dict eligible for checking when we hit 'h' next time
        if letter == 'e' and wordcomplete == 0:
            wordcomplete = 1
        
        if letter == 'h' and wordcomplete > 0:
            # reset flag
            wordcomplete = 0
            result = verifypass(adict)
            if result == -1:
                print 'Invalid for:',string
            else:
                adict = {}

        if letter not in adict:
            adict[letter] = 1
        else:
            adict[letter] += 1

    # check for last pass
    result = verifypass(adict)
    if result == -1:
        print 'Invalid for:',string
    else:
        print 'Valid for:',string

def verifypass(adict):
    # some char missing
    if len(adict) < 4 or len(set(adict.values())) != 1:
        return -1
    return 1

def main():
    check('hhiirree')
    check('hire')
    check('hhiirreee')
    check('hired')
    check('hhiirrree')
    check('hirehhiirree')
    check('hiredhiirreeddhiree')
    check('hie')

if __name__ == '__main__':
    main()