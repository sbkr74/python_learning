# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
my_tuple = ('Java','Python','SQL','Scala','Spark','HDFS','YARN')
my_tuple = list(my_tuple)
my_tuple.append('kubernetes')
my_tuple[0] = 'Bash'
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
