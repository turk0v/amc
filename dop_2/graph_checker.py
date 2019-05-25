def check_connectivity():
	pass

def check_cyclic(g):
    """
    Return True if the directed graph g has a cycle.
    """
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)

gr = {0: (1,), 1: (2,), 2: (0,3)}

print(check_cyclic(gr))

def total_checker(graph):
	if (check_cyclic(graph) == True):
		return True
	else:
		return False





