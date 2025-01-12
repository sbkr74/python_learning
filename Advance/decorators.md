## Decorators

Python Decorators are a powerful and expressive tool in Python that allows you to modify the behavior of a function or method. They are often used to add "wrapping" functionality to existing functions in a clean and readable way.

Decorators are the most common use of higher-order functions in Python. It allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

### Why Python decorators rather than closures?
Python decorators are preferred over closures for their readability, reusability, and flexibility. Decorators clearly convey the intent of modifying a function with the @decorator_name syntax, keeping the code clean and focused. They promote modularity, allowing the same decorator to be easily reused across multiple functions. Decorators can also preserve the original function's metadata, which is important for debugging. Additionally, decorators can be parameterized and stacked to compose various behaviors efficiently, making them a more powerful and versatile tool compared to closures.

### How Decorators Work
A decorator is a function that takes another function as an argument, adds some kind of functionality, and returns a new function. Here's a basic example of a decorator:

## Differences between Closures And Decorators In Python

```
Aspect      |   Closures    |   Decorators

Definition  |Function with access to its lexical scope.     | Higher-order function that modifies another function.

Purpose     |Retain access to variables in enclosing scope. | Add functionality to existing functions.

Usage       |Retain state after the outer function finishes.| Modify behavior of functions or methods.

Syntax      |   Nested function captures local variables.   | Applied with @ syntax above a function.

Focus       |       Capturing state.                        | Extending behavior.
```