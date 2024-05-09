# in python either it is single character or group of character(words,sentence).
# it is treated as string
# it can be within single quotes,double quotes or triple quoutes
s = 'a'
s1 = "this is a example string"
s2 = '''example of 
multi-line string'''

print(s)
print(s1)
print(s2)

# String Concatenation
first_name = 'Python'
last_name = 'programming'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)


#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t2\t5')
print('Day 3\t3\t8')
print('Day 4\t4\t20')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')