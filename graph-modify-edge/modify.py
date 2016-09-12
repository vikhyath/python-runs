# Given an undirected graph and a node, modify the graph into a directed graph 
# such that, any path leads to one particular node.

#!/usr/bin/env python

graph = {
	'A': ['B', 'E'], 
	'B': ['A', 'C'],
	'C': ['B', 'D'],
	'D': ['G', 'C'],
	'G': ['F', 'D'],
	'F': ['E', 'G'],
	'E': ['A', 'F']
}