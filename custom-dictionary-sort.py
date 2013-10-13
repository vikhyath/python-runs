# 1) Sort the input character array based on the dictionary given.

# For eg If input word is SHEEP, sorting will make it as EEHPS.

# But in the dictionary, E may not be at first. As per the dictionary, if P is first, S followed and E later and finally H.

# Then sorted array is PSEEH.

from sys import argv, exit

adict = {'P': 1, 'S': 2, 'E': 3, 'H': 4}

def customsort(x):
	return adict[x]

def main():
	if len(argv) < 2:
		print 'USAGE: python file.py string'
		exit(0)

	string = sorted(argv[1], key = lambda x: customsort(x))
	print ''.join(string)

if __name__ == '__main__':
	main()