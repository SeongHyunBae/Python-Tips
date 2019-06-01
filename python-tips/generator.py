## Generator ##
# Generator is function which generate iterator
# Characteristic
# 1. Every generator is iterator.
# 2. The next value in the sequence is calculated as needed.
# 3. The internal state of function is maintained through internal variables.
# 4. You can model objects with infinite order

def generator():
	print 'return 1'
	yield 1
	print 'return 2'
	yield 2
	print ' return 3'
	yield 3

gen = generator()
print type(gen)

print next(gen)
print next(gen)
print next(gen)

# when 'yield' is called, it is implicitly called return, and once it is executed,
# it excutes the following code.

gen = generator()
for i in gen:
	print i

# Infinite generator

def inf_generator():
	count = 0
	while True:
		count += 1
		yield count

gen = inf_generator()

for n, i in enumerate(gen):
	print n, i
	if n > 10:
		break

def three_generator():
	a = [1, 2, 3]
	for i in a:
		yield i
print list(three_generator())