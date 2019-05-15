
# example 1
# *args is used to send a non-keyworded variable length argument list to the function.
def f(*arg):
	print arg
	print arg[0]
	print arg[1]
	print arg[2]

f(1,2,3)
####### result #######
# (1, 2, 3)
# 1
# 2
# 3




# example 2
# **kwargs is used to pass keyworded variable length of arguments to a function.
def f(**kwargs):
	print kwargs

f(a=1, b=2, c=3, d=4)
####### result #######
# {'a': 1, 'c': 3, 'b': 2, 'd': 4}




# example 3
# *arg + **kwargs
def f(*arg, **kwargs):
	print arg
	print kwargs

f(1,2,3, a=1, b=2, c=3, d=4)
####### result #######
# (1, 2, 3)
# {'a': 1, 'c': 3, 'b': 2, 'd': 4}




