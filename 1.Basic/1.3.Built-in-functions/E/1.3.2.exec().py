# exec(object, globals=None, locals=None, /, *, closure=None)
'''
This function supports dynamic execution of Python code. object must be either a string or a code object. 
If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input
'''

'''
Be aware that the nonlocal, yield, and return statements may not be used outside of function definitions 
even within the context of code passed to the exec() function. The return value is None.
'''