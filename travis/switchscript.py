#!/usr/bin/python
from sys import argv, exit
import re

def main():
    if len(argv[:]) < 3:
        print 'Usage: python script-name.py input-file output-file.csv'
        exit()
    
    ip = argv[1]
    op = argv[2]
    newline = 0
    moduleseen = 0
    with open(op, 'w') as o:
        o.write('Timestamp,')
        for i in xrange(9):
            o.write('Policy,Module 1,Module 2,Module 3,Module 4,Module 7,Module 8,')
        with open(ip, 'r') as f:
            for line in f:
                line = line.strip()

                # if module seen is set to true, print the current line and go to next
                if moduleseen == 1:
                    moduleseen = 0
                    alist = re.findall(r'\d{1,}', line)
                    o.write(''.join(alist) + ',')
                    continue


                # if module seen, ignore current and fetch next
                alist = re.findall(r'module\s\d\s:', line)
                if len(alist) > 0:
                    moduleseen = 1
                    continue

                # get timestamp
                alist = re.findall(r'^\d{1,}:\d{1,}:\d{1,}.*', line)
                if len(alist) > 0:
                    # print newline only at the beginning, that is do not print newline while exit switch
                    newline = not newline
                    if newline > 0:
                        o.write('\n')
                        o.write(''.join(alist) + ',')
                    continue

                # if class-map is seen, print
                alist = re.findall(r'\bclass-map\b.*', line)
                if len(alist) > 0:
                    o.write(''.join(alist) + ',')

if __name__ == '__main__':
    main()