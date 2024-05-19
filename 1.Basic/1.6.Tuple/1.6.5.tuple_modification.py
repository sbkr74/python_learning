# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
my_tuple = ('Java','Python','SQL','Scala','Spark','HDFS','YARN')
my_tuple = list(my_tuple)
my_tuple.append('kubernetes')   # append()
my_tuple[0] = 'Bash'            # index
my_tuple.insert(5,'Docker')     # insert()
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple = list(my_tuple)
my_tuple.remove('YARN')         # remove()
my_tuple.remove(my_tuple[1])    # remove() index
my_tuple.pop()                  # pop()
my_tuple.pop(2)                 # pop() index
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple = list(my_tuple)
my_tuple.clear()                # clear() to empty the tuple
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Deleting Tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
del my_tuple