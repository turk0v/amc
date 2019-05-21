import unittest
from hw1_prac_turkov_matvei_777 import my_merge_few,merge_sort

class TestAlgo(unittest.TestCase):
	def test_merge(self):
		self.assertEqual(my_merge_few([1,2,3],[4],[5,6],[7]),[1,2,3,4,5,6,7])

	def test_merge_empty(self):
		self.assertEqual(my_merge_few([]),[])

	def test_merge_sort(self):
		self.assertEqual(merge_sort([5,4,3,2,6,1]),[1,2,3,4,5,6])

	def test_merge_sort_empty(self):
		self.assertEqual(merge_sort([]),[])

	def test_merge_sort_one(self):
		self.assertEqual(merge_sort([1]),[1])


if __name__ == '__main__':
	unittest.main() 