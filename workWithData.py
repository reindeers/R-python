# see "data from scratch"

from matplotlib	import pyplot as plt
import random
import sys
import math
from collections import Counter


# Exploring the data
## one-dimensional data

def bucketsize(point, bucket_size):
	return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
	return Counter(bucketsize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
	histogram = make_histogram(points, bucket_size)
	plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
	plt.title(title)
	plt.show()

random.seed(0) #?

#uniform between -100 and 100
uniform	= [200 * random.random() - 100 for _ in range(10000)]

# normal distribution with mean 0, standard	deviation 57
normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform Histogram")
plot_histogram(normal, 10, "Normal Histogram")

## two dimensional data

def random_normal():
	"""returns a random draw from a standard normal distribution"""
	return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker = ".", color="black", label="ys1")
plt.scatter(xs, ys2, marker = ".", color="gray", label="ys2")

plt.xlabel("xs")
plt.ylabel("ys")
plt.legend(loc=9)
plt.show()

print correlation(xs, ys1)
print correlation(xs, ys2)
## many dimensional data

