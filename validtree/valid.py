# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

def valid(edges):
	if not len(edges):
		return False

	pending = {}
	visited = {}
	for edge in edges:
		# need to check both to make sure we only account for pending visits,
		# that is check the case of a forest and not a tree
		if edge[0] not in pending and edge[0] not in visited:
			pending[edge[0]] = 1

		# already visited so need to return negative
		# checks for circular loop
		if edge[1] in visited or edge[1] in pending:
			return False

		visited[edge[1]] = 1

	# return false is there are more than one pending visits, which means
	# this is a forest
	return False if len(pending) > 1 else True

print(valid([[0, 1], [0, 2], [0, 3], [1, 4]]))
print(valid([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(valid([[0, 1], [1, 2], [2, 3], [1, 3], [3, 0]]))
print(valid([[0, 1], [0, 2], [0, 3], [1, 4], [5, 6]]))
print(valid([]))
