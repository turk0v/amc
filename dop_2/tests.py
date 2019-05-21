import unittest
from planar_graph import Graph,graph_creator
from graph_checker import check_cyclic

class GraphTest(unittest.TestCase):
	
	def test_graph_build(self):
		test_graph = graph_creator('test_graph.txt')
		res_graph = str({0: (3, 4, 5), 1: (3, 4, 5), 2: (3, 4, 5), 3: (), 4: (), 5: ()})
		self.assertEqual(test_graph.__str__(),res_graph)

	def test_graph_cycle(self):
		test_graph_true = {0: (1,), 1: (2,), 2: (0,3)}
		test_graph_false = {0: (1,), 1: (2,), 2: (3,)}
		self.assertTrue(check_cyclic(test_graph_true))
		self.assertFalse(check_cyclic(test_graph_false))

	def test_graph_is_connected(self):
		test_graph = graph_creator('test_graph.txt')
		self.assertFalse(test_graph.is_connected())