# For a given string and dictionary, how many sentences can you make 
# from the string, such that all the words are contained in the dictionary. 

# // eg: for given string -> "appletablet" 
# // "apple", "tablet" 
# // "applet", "able", "t" 
# // "apple", "table", "t" 
# // "app", "let", "able", "t" 

# // "applet", {app, let, apple, t, applet} => 3 
# // "thing", {"thing"} -> 1


def make(string, dictionary, mapper={}):
	end = 0
	alist = []
	if string in mapper:
		return mapper[string]
	while end < len(string):
		if string[:end+1] in dictionary:
			alist.append(string[:end+1])

			if end + 1 < len(string):
				gotlist = make(string[end+1:], dictionary)
				idx = 0
				while idx < len(gotlist):

					gotlist[idx] = string[:end+1] + ' ' + gotlist[idx]
					idx += 1

				if len(gotlist):
					alist.pop()

				alist += gotlist

		end += 1

	mapper[string] = alist
	return alist


print(make('appletablet', ['app', 'let', 'apple', 'applet', 't', 'able', 'tablet', 'table']))