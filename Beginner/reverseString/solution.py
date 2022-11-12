# chain methods
# time: O(n)
# space: n
def reverseStringMeth(s : str) -> str:
    rev = [*s]
    rev.reverse()
    return ''.join(rev)

# slicing
# time: O(n)
# space: n
def reverseStringSlice(s : str) -> str:
    return "test"[::-1]

# recursive
# time: O(n)
# space: n
def reverseStringRecursive(my_string):
   if len(my_string) == 0:
      return my_string
   else:
      return reverseStringRecursive(my_string[1:]) + my_string[0]

# reduced
# time: O(n)
# space: n
def reverseStringReduce(s : str) -> str:
    import functools
    return functools.reduce(lambda acc, curr: curr + acc, [*s])