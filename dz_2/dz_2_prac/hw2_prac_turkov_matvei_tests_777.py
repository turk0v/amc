import unittest
from hw2_prac_turkov_matvei_code_777 import straight_multiplication,strassen_multiplication
import numpy as np

class TestAlgo(unittest.TestCase):
	
	def test_strasssen(self):
		a = np.random.randint(0, 10, size=(16, 16))
		b = np.random.randint(0, 10, size=(16, 16))
		self.assertEqual((strassen_multiplication(a, b) - straight_multiplication(a, b)).all(),0)

	def test_strasssen_one(self):
		a = np.random.randint(0, 10, size=(1, 1))
		b = np.random.randint(0, 10, size=(1, 1))
		self.assertEqual((strassen_multiplication(a, b) - straight_multiplication(a, b)).all(),0)

if __name__ == '__main__':
	unittest.main() 