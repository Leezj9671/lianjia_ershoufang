import csv
import numpy as np
import matplotlib.pyplot as plt

price, size = np.loadtxt('house.csv', delimiter='|', usecols=(1, 2), unpack=True)
print(price, size)

price_mean = np.mean(price)
size_mean = np.mean(size)

print('average price: {}'.format(price_mean))
print('average size: {}'.format(size_mean))

price_var = np.var(price)
size_var = np.var(size)

print('var price: {}'.foramt(price_var))
print('var size: {}'.foramt(size_var))

plt.figure()
plt.subplot(211)
plt.title("/ 1W RMB")
plt.hist(price, bins=20)

plt.subplot(212)
plt.xlabel("/ m^2")
plt.hist(size, bins=20)

plt.figure(2)
plt.title("price")
plt.plot(price)

plt.show()
