import csv
import numpy
import matplotlib.pyplot as pyplot

price, size = numpy.loadtxt('house.csv', delimiter='|', usecols=(1, 2), unpack=True)
print(price, size)

price_mean = numpy.mean(price)
size_mean = numpy.mean(size)

print('average price: {}'.format(price_mean))
print('average size: {}'.format(size_mean))

price_var = numpy.var(price)
size_var = numpy.var(size)

print('var price: {}'.foramt(price_var))
print('var size: {}'.foramt(size_var))
