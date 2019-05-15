import functools

# example 1
# Function composition is used to combine functions such that the result of
# each function is passed as the argument of the next function. 
def compose2(f, g):
	return lambda x: f(g(x))

def add_1(x):
	return x + 1

def mul_10(x):
	return x * 10

def minus_2(x):
	return x - 2

print compose2(add_1, mul_10)(3)
print compose2(compose2(add_1, mul_10), minus_2)(3)
####### result #######
# 31
# 11




# example 2
# The reduce function is used to apply a particular function passed in
# its argument to all of the list elements.
# [a1, a2, a3, a4, a5] -> func(func(func(func(a1, a2), a3), a4), a5)
lis = [1, 2, 3, 4, 5]

print functools.reduce(lambda a, b : a + b, lis)
####### result #######
# 15




# example 3
def compose(*func):
	def compose2(f, g):
		return lambda x: f(g(x))
	return functools.reduce(compose2, func, lambda x: x)

print compose(add_1, mul_10, minus_2)(3)
####### result #######
# 11




# example 4
def compose(*func):
	return functools.reduce(lambda f, g: lambda x: f(g(x)), func, lambda x: x)

f = compose(add_1, mul_10, minus_2)

print f(3)
####### result #######
# 11
