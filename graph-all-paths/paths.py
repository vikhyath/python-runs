graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

# def allpaths(graph, start, end, paths, globalpaths=None):
# 	if start == end:
# 		return [start] + paths

# 	if start not in graph:
# 		return None

# 	print(graph[start])
# 	for node in graph[start]:
# 		localpath = []
# 		if node not in paths:
# 			currpath = allpaths(graph, node, end, paths)
# 			paths.append(currpath)
# 			globalpaths.append(paths)

# 		return paths

# 	return globalpaths

def all_paths(graph, start, end, paths):
	globalpaths = []
	paths = paths + [start]
	if start == end:
		return [paths]

	if start not in graph:
		return None

	for node in graph[start]:
		currpath = all_paths(graph, node, end, paths)
		for path in currpath:
			globalpaths.append(path)
			
	return globalpaths

def one_path(graph, start, end, paths):
	paths.append(start)
	if start == end:
		return paths

	if start not in graph:
		return None

	for node in graph[start]:
		if node not in paths:
			one_path(graph, node, end, paths)
			return

	return None

paths = []
#one_path(graph, 'A', 'D', paths)
#print(paths)

print(all_paths(graph, 'A', 'D', paths))