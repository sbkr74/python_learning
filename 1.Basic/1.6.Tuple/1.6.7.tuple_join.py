# joining tuples can be done only using `+` operator
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)
print(type(tpl3))