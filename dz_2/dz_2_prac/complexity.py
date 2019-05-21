from datetime import datetime
from hw2_prac_turkov_matvei_code_777 import straight_multiplication,strassen_multiplication
import numpy as np

start_time = datetime.now()
a = np.random.randint(0, 10, size=(16, 16))
b = np.random.randint(0, 10, size=(16, 16))
straight_multiplication(a,b)
end_time = datetime.now()
print('Duration straight on 16x16: {}\n'.format(end_time - start_time))

start_time = datetime.now()
a = np.random.randint(0, 10, size=(16, 16))
b = np.random.randint(0, 10, size=(16, 16))
strassen_multiplication(a,b)
end_time = datetime.now()
print('Duration strassen on 16x16: {}\n'.format(end_time - start_time))

start_time = datetime.now()
a = np.random.randint(0, 10, size=(64, 64))
b = np.random.randint(0, 10, size=(64, 64))
straight_multiplication(a,b)
end_time = datetime.now()
print('Duration straight on 64x64: {}\n'.format(end_time - start_time))

start_time = datetime.now()
a = np.random.randint(0, 10, size=(64, 64))
b = np.random.randint(0, 10, size=(64, 64))
strassen_multiplication(a,b)
end_time = datetime.now()
print('Duration strassen on 64x64: {}\n'.format(end_time - start_time))

start_time = datetime.now()
a = np.random.randint(0, 10, size=(512, 512))
b = np.random.randint(0, 10, size=(512, 512))
straight_multiplication(a,b)
end_time = datetime.now()
print('Duration straight on 512x512: {}\n'.format(end_time - start_time))

start_time = datetime.now()
a = np.random.randint(0, 10, size=(512, 512))
b = np.random.randint(0, 10, size=(512, 512))
strassen_multiplication(a,b)
end_time = datetime.now()
print('Duration strassen on 512x512: {}\n'.format(end_time - start_time))

