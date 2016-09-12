# Given an api which returns an array of chemical names 
# and an array of chemical symbols, display the chemical names 
# with their symbol surrounded by square brackets: 

# Ex: 
# Chemicals array: ['Amazon', 'Microsoft', 'Google'] 
# Symbols: ['I', 'Am', 'cro', 'Na', 'le', 'abc'] 

# Output: 
# [Am]azon, Mi[cro]soft, Goog[le] 

# If the chemical string matches more than one symbol,
#  then choose the one with longest length.
#   (ex. 'Microsoft' matches 'i' and 'cro') 

#!/usr/bin/env python

array = ['Amazon', 'Microsoft', 'Google'] 
symbols = ['I', 'Am', 'cro', 'Na', 'le', 'abc'] 

values = {}

for symbol in symbols:
	for name in array:
		idx = name.find(symbol)

		if idx == -1 or (name in values and values[name]['length'] > len(symbol)):
			continue

		coded = name[:idx] + '[' + name[idx:idx+len(symbol)] + ']'
		if idx + len(symbol) < len(name):
			coded += name[idx + len(symbol):]

		values[name] = {
			'length': len(symbol),
			'coded': coded
		}

print(values)