import re

x = 'this is not a bad choice'

#compile a pattern
pattern = re.compile('not.*bad', re.I) # re.I says ignore case

#search for that pattern in x and return the *first* match that satisfies condition
y = pattern.search(x); #will return the match object <_sre.SRE_Match object at 0x101e3d238>

# The match() function only checks if the RE matches at the beginning of the string while search() will 
# scan forward through the string for a match. Its important to keep this distinction in mind. 
# Remember, match() will only report a successful match which will start at 0 if the match wouldnt start at zero,
# match() will not report it.

#using this match object we can get info like
print y.group() # matching string
print y.start() # starting index of match
print y.end() # ending index of the match


y = pattern.findall(x)
print y # will return a list element that contains the match, if no match then returns empty list

print '###iterable'
y = pattern.finditer(x)
for str in y:
	print str.group() # will print each match
print '###iterable'

# now if we want to do a substitution, we can call re.sub('word', x)
k = pattern.sub('good', x) # specifying a third argument count=1 will limit replacements to 1
print k # will print this is good choice

# subn('word', x) will return the number of replacements

# trying a check for word boundaries
newpattern = re.compile('\bnot\b.*\bbad\b', re.I)
print newpattern.search(x) # WILL PRINT NONE !!!  why? because \b in python literals means backspace. Hence to avoid that collision
# between python literals and regex, we need to give r -> rawinput

newpattern = re.compile(r'\bnot\b.*\bbad\b', re.I)
print newpattern.search(x)

############################################## ALTERNATE WAY without using compile #######################################
regexp = '\\bnot\\b.*\\bbad\\b'
### another way without using escape is to add the raw flag
regexp1 = r'\bnot\b.*\bbad\b'
print regexp
print regexp1
print re.finditer(regexp, x) # need to pass regex everytime
print re.sub(regexp, 'good', x) # instead of this, use compile