# this is reading from a file
from sys import argv
script, file = argv

txt = open(file, 'r+')
print 'contents of file %r are' % file

for line in txt:
  print line,
  
txt.close()
txt = open(file, 'r+')
print 'contents can also be read as'
print '%sAND ALSO AS' %txt.readline()
print txt.read()

with open(file, 'r+') as f:
  f.seek(0, 2)
  f.write('gibberish text')

print f.closed #returns true