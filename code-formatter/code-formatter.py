# program reads an input file named input.txt and ensures no more than SIZE number
#	of chars per line are present
# if more lines are present then split at space, insert / wherever we want to split
# if space is found after the SIZE allowed chars, split after. Let us say SIZE is 5
#	and space is found at 7th, split at 7th
# output is written to output.txt

import re

def format(line, SIZE=5):

	# if line size is not > SIZE dont do anything
	if (len(line) > SIZE):
		# form a regex
		pattern = re.compile(r'\s')
		matches = pattern.findall(line)

		# check if a space exists
		if len(matches) >= 1:

			# easier to perform operations on list
			newline = list(line)

			# stitch multiple splits in line if necessary
			stitchedline = None
			splitpoint = 0

			# if lucky, we found the space at the correct index, yay!
			if newline[SIZE] == ' ':
				newline[SIZE] = '/'
				splitpoint = SIZE
			# else, oh boy! go search either the lower/upper part before/after SIZE
			else:

				# determine lower part or upper part to search for
				# if characters do not match white space in the set of chars < size then search in upper
				# else if matches then search in lower
				start = SIZE
				end = -1 # search through 0th character
				increment = -1 # from end to start

				lower = pattern.findall(''.join(newline[:SIZE]))

				# no whitespace in lower, hence search upper
				if len(lower) == 0:

					# find in upper
					start = SIZE+1
					end = len(newline)
					increment = 1

				for index in xrange(start, end, increment):
					if newline[index] == ' ':
						newline[index] = '/'
						splitpoint = index
						break

			# recursive calls, to split again if needed, maybe the line has 2000 chars, account for this case
			# stitch individual splits together
			stitchedline = ''.join(newline[:splitpoint+1])
			stitchedline += format(''.join(newline[splitpoint+1:]))
			line = stitchedline
	return line

def main():
	try:
		with open('input.txt', 'r') as f:
			with open('output.txt', 'w') as fw:
				for line in f:
					newline = format(line.rstrip())
					fw.write(newline+'\n')
	except IOError:
		print 'unable to find input.txt for reading or create a file output.txt for writing'

if __name__ == '__main__':
	main()