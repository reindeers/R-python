height_weight_age = [70, # inches,
					 170, # pounds,
					 40 ] # years
grades = [95, # exam1
		 80, # exam2
		 75, # exam3
		 62 ] # exam4

# vectors

def vector_add(v, w):
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_substract(v, w):
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	s = vectors[0]
	for vector in vectors[1:]:
		s = vector_add(s, vector)
	return s

def scalar_multiply(c, v):
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	return sum(w_i, v_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
	return dot(v, v)

import math

def magnitude(v):
	return math.sqrt(sum_of_squares(v))


def distance(v, w):
	return magnitude(vector_subtract(v,	w))


# matrices

