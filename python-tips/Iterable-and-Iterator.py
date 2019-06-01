## Iterable ##

# Iterable object is repeatable object.
# ex) list, dict, set, str, bytes, tuple, range

# Iterator
# Iterator object can take out value in sequence.
# Iterator can make iterable object with built-in function or iterable object`s method.
# ex) built-in function : iter()

# Iterator can make iterable object with built-in function
a = [1, 2, 3]
a_iter = iter(a)
print type(a_iter)

# Iterable object has __iter__ method which can make iterator.
b = {1, 2, 3}
print dir(b)
b_iter = b.__iter__()
print type(b_iter)


print next(a_iter)
print next(a_iter)
print next(a_iter)

print b_iter.next()
print b_iter.next()
print b_iter.next()