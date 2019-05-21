
class Polynomial:

	def __init__(self, *coef):
		self.coef = coef
	
	def __repr__(self):
		res = ""
		for index,coef in enumerate(self.coef):
			if index == 0:
				res += str(coef)
			elif (index == 1):
				res += f"+({coef}x)"
			else:
				res += f"+({coef}x^{index})"
		return str(res)

	def degree(self):
		return(len(self.coef)-1)


	def check_equal(self,polynomial):
		polynomial.make_equal_degree(self)
		result_flag = True
		for i in range(len(self.coef)):
			if self.coef[i] == polynomial.coef[i]:
				pass
			else:
				result_flag = False
		return(result_flag)

	def add_value(self,polynomial):
		polynomial.make_equal_degree(self)
		final_poly = Polynomial()
		for i in range(len(polynomial.coef)):
			final_poly.add_coef(self.coef[i]+polynomial.coef[i])
		return(final_poly)


	def add_coef(self,new_coef):
		self.coef+=(new_coef,)

	def make_equal_degree(self,polynomial):
		degree_first = self.degree()
		degree_second = polynomial.degree()
		if (degree_first > degree_second):
			for _ in range(degree_first-degree_second):
				polynomial.add_coef(0)
		elif(degree_second > degree_first):
			for _ in range(degree_second-degree_first):
				self.add_coef(0)
		else:
			pass

	def substract_value(self,polynomial):
		polynomial.make_equal_degree(self)
		final_poly = Polynomial()
		for i in range(len(polynomial.coef)):
			final_poly.add_coef(self.coef[i]-polynomial.coef[i])
		return(final_poly)


	def pow_power(self,power):
		pass

	def multiply_poly(self,poly):
		pass


class FFT():

	def __init__(self, arg):
		super(FFT, self).__init__()
		self.arg = arg

	def get_root(self):
		pass

	def fourier_transform(self):
		pass

	def inverse_fourier_transform(self):
		pass


	def add_padding(self):
		pass

	def fast_ft(self):
		pass

	def fast_inverse_ft(self):
		pass




class Substring_match():

	def __init__(self, arg):
		super(Substring_match, self).__init__()
		self.arg = arg

	def find_substring(self):
		pass

	def find_match(self):
		pass
		









