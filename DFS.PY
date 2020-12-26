

from collections import defaultdict




class Graph:

	def __init__(self):


		self.graph = defaultdict(list)


	def ADD_EDGE(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):

	
		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	
	def DFS(self, v):


		visited = set()

		self.DFSUtil(v, visited)





g = Graph()
g.ADD_EDGE(0,3)
g.ADD_EDGE(0,2)
g.ADD_EDGE(1,3)
g.ADD_EDGE(2,3)
g.ADD_EDGE(2, 1)
g.ADD_EDGE(3, 2)

print("DEPTH FIRST SERCH RESULT IS STARTING FROM VERTEX FIRST")
g.DFS(1)

