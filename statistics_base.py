import math
import sys
from collections import Counter

num_friends	= [100, 49, 45, 24, 10, 5, 31, 8, 16, 8, 8, 16, 16]
daily_minutes = [20, 30, 1, 2, 3, 5, 80, 11, 10, 12, 14, 20, 1]

def dot(v, w):
	return sum(v_i * w_i for v_i, w_i in zip(v, w))
# Statistics

f_number = len(num_friends)

f_min = min(num_friends)
f_max = max(num_friends)

def sum_of_squares(x):
	return sum(x_i*x_i for x_i in x)

def mean(x):
	return sum(x) / len(x)

def median(x):
	sort_x = sorted(x)
	if len(x) % 2 == 1:
		return sort_x[len(x)//2]
	else:
		return (sort_x[len(x)] + sort_x[(len(x)-1)]) / 2

def quantile(x, p):
	sort_x = sorted(x)
	return sort_x[int(len(x) * p)]

def mode(x):
	counts = Counter(x)
	m_cnt = max(counts.values())
	print [x_i for x_i, cnt in counts.iteritems()
			if cnt == m_cnt]

## dispersion

def data_range(x):
	return max(x) - min(x)

def de_mean(x):
	return [x_i - mean(x) for x_i in x]

def variance(x):
	dev = de_mean(x)
	return sum_of_squares(dev) / (len(x)-1)

def standart_deviation(x):
	return math.sqrt(variance(x))

## Corelation

def covariance(x, y):
	return dot(de_mean(x), de_mean(y)) / (len(x)-1)

def correlation (x, y):
	stdev_x = standart_deviation(x)
	stdev_y = standart_deviation(y)
	if stdev_y > 0 and stdev_x > 0:
		return covariance(x, y) / stdev_x / stdev_y
	else:
		return 0

f_mean = mean(num_friends)
f_median = median(num_friends)
f_quantile = quantile(num_friends, 0.5)
f_mode = mode(num_friends)
f_data_range = data_range(num_friends)
f_standart_deviation = standart_deviation(num_friends)
f_covariance = covariance(num_friends, daily_minutes)
f_correlation = correlation(num_friends, daily_minutes)
