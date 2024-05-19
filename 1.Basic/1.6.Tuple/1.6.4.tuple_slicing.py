# slicing 
my_tuple = ('Java','Python','SQL','Scala','Spark','HDFS','YARN')
print(my_tuple[0:7])                # all items
print(my_tuple[0:])                 # all items
print(my_tuple[0:len(my_tuple)])    # all items
print(my_tuple[2:5])                # ('SQL', 'Scala', 'Spark')

# using negative index
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1] 
print(all_items)
print(middle_two_items)