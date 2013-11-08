# this is reading from a file
from sys import argv
script, file = argv

txt = open(file, 'r+')
print 'contents of file %r are' % file

for line in txt:
  print line,
  
txt.close()
txt = open(file, 'r+')

# The first argument is a string containing the filename. 
# The second argument is another string containing a few characters describing the way in which the file will be used. 
# mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), 
# and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. 
# The mode argument is optional; 'r' will be assumed if it’s omitted.

print 'contents can also be read as'
print '%sAND ALSO AS' %txt.readline()
print txt.read()

with open(file, 'r+') as f:
  f.seek(0, 2)
  f.write('gibberish text')

print f.closed #returns true