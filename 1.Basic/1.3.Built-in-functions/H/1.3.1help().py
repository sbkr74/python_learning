'''
Invoke the built-in help system. If no argument is given, the interactive help system starts on the interpreter console. 
If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or 
documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object 
is generated.
'''

print(help())
print(help(str))