import unittest
from fft_code import Polynomial

class TestPolynomial(unittest.TestCase):
	
	def test_creation(self):
		poly = Polynomial(1,2,3)
		self.assertEqual(str(poly),"1+(2x)+(3x^2)")

	def test_degree(self):
		poly = Polynomial(1,2,4,5,5,6)
		self.assertEqual(poly.degree(),5)

	def test_equal_true(self):
		poly1 = Polynomial(1,2,3,4,5)
		poly2 = Polynomial(1,2,3,4,5)
		self.assertEqual(poly1.check_equal(poly2),True)

	def test_equal_false(self):
		poly1 = Polynomial(1,2,3,4,5,6,7)
		poly2 = Polynomial(1,2,3,4,5,8,12,34)
		self.assertEqual(poly1.check_equal(poly2),False)

	def test_add_value(self):
		poly1 = Polynomial(1,2,3)
		poly2 = Polynomial(5,0,0,1)
		self.assertEqual(str(poly1.add_value(poly2)),"6+(2x)+(3x^2)+(1x^3)")

	def test_substract_value(self):
		poly1 = Polynomial(1,2,3)
		poly2 = Polynomial(1,2,0,1)
		self.assertEqual(str(poly1.substract_value(poly2)),"0+(0x)+(3x^2)+(-1x^3)")

	
		



if __name__ == '__main__':
	unittest.main() 