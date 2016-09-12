class Graph:
	def __init__(self, nodes):
		self.nodes = nodes
		self.distance = {}
		self.edges = {}

	def addEdge(self, start, end, distance):
		if start not in self.edges:
			self.edges[start] = []
		self.edges[start].append(end)

		if end not in self.edges:
			self.edges[end] = []
		self.edges[end].append(start)

		self.distance[(start, end)] = distance
		self.distance[(end, start)] = distance

	def walkAgain(self, startNode):
		visited = {}
		visited[startNode] = 0
		unvisited = set(self.nodes)

		while(len(unvisited) > 1):	
			minNode = None
			for node in unvisited:
				if node in visited:
					if not minNode:
						minNode = node

					if visited[node] < visited[minNode]:
						minNode = node

			if not minNode:
				break

			unvisited.remove(minNode)
			weight = visited[minNode]
			for node in self.edges[minNode]:
				if node in unvisited and (node not in visited or visited[node] > weight + self.distance[(minNode, node)]):
					visited[node] = weight + self.distance[(minNode, node)]

		print(visited)

	def walk(self, startNode):
		self.visited = {}
		self.visited[startNode] = 0
		unvisited = set(self.nodes)

		while(len(unvisited) > 1):
			minNode = None
			for node in unvisited:
				if node in self.visited:
					if not minNode:
						minNode = node

					if self.visited[node] < self.visited[minNode]:
						minNode = node

			if not minNode:
				break

			unvisited.remove(minNode)
			weight = self.visited[minNode]
			for vertex in self.edges[minNode]:
				if vertex in unvisited and (vertex not in self.visited or self.visited[vertex] > weight + self.distance[(minNode, vertex)]):
					self.visited[vertex] = weight + self.distance[(minNode, vertex)]

graph = Graph((1, 2, 3, 4, 5, 6))
graph.addEdge(1, 2, 7)
graph.addEdge(1, 6, 14)
graph.addEdge(1, 3, 9)
graph.addEdge(2, 3, 10)
graph.addEdge(2, 4, 15)
graph.addEdge(3, 4, 11)
graph.addEdge(3, 6, 2)
graph.addEdge(6, 5, 9)
graph.addEdge(5, 4, 6)

print(graph.nodes)
print(graph.distance)
print(graph.edges)

# graph.walk(1)

# print(graph.visited)
graph.walkAgain(1)