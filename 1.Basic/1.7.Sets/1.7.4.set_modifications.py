st = {'item1','item2','item3','item4','item5','item7'}

# adding item in set
st.add('item6')
print(st,len(st))

# adding multiple items in set
st.update(['item8','item9','item10'])
print(st,len(st))

# removing item from set
st.remove('item1')
print(st,len(st))

# pop() removes random item from list
removed_item = st.pop()
print(removed_item)
print(st,len(st))

# clear the set/ empty the set
st.clear()
print(st,len(st))

# delete a set
del st