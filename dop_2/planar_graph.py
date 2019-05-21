class Graph(object):

	def __init__(self,vertices,edges):
		self.vertices = vertices
		self.edges = edges
		self.graph_dict = {}

	def add_connection(self,vertice1,vertice2):
		if len(self.graph_dict.keys()) > self.vertices:
			print('Wrong vertices number')
			return
		real_edges = sum([len(value) for value in self.graph_dict.values()])
		if real_edges > self.edges:
			print('Wrong edges number')
			return
		else:
			if vertice1 not in self.graph_dict.keys():
				self.graph_dict[vertice1] = (vertice2,)
			else:
				self.graph_dict[vertice1] = self.graph_dict[vertice1] + (vertice2,)

		val_dict = []
		for patch in self.graph_dict.values():
			for elem in patch:
				if elem not in val_dict:
					val_dict.append(elem)
				else:
					pass 

		if self.graph_dict.keys() != val_dict:
			diff_vertices = list(set(val_dict) - set(self.graph_dict.keys()))
			for vertice in diff_vertices:
				self.graph_dict[vertice] = ()

	def sort_graph_keys(self):
		self.graph_dict = dict(sorted(self.graph_dict.items()))


	def is_connected(self, vertices_encountered = None, start_vertex=None):
			"""Check graph connectivity"""
			if vertices_encountered is None:
				vertices_encountered = set()    
			vertices = list(self.graph_dict.keys())
			if not start_vertex:
				start_vertex = vertices[0]
			vertices_encountered.add(start_vertex)
			if len(vertices_encountered) != len(vertices):
				for vertex in self.graph_dict[start_vertex]:
					if vertex not in vertices_encountered:
						if self.is_connected(vertices_encountered, vertex):
							return True
			elif (vertices == list(vertices_encountered)):
				return True
			return False

	def __str__(self):
		return(str(self.graph_dict))


def graph_creator(filename):
	with open(filename,'r') as file:
		graph_info = file.readline().split(' ')
		vertices = int(graph_info[0])
		edges = int(graph_info[1])
		graph = Graph(vertices,edges)

		for line in file:
			graph_pair = line.split(' ')
			vertice_out = int(graph_pair[0])
			vertice_in = int(graph_pair[1])
			graph.add_connection(vertice_out,vertice_in)
	graph.sort_graph_keys()
	return graph

