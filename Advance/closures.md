## Closures in Python
A Closure in Python occurs when a nested function captures the local variables from its enclosing scope. This allows the nested function to access these variables even after the outer function has finished executing.

In Python, a closure is a powerful concept that allows a function to remember and access variables from its lexical scope, even when the function is executed outside that scope. Closures are closely related to nested functions and are commonly used in functional programming, event handling and callbacks.

A closure is created when a function (the inner function) is defined within another function (the outer function) and the inner function references variables from the outer function. Closures are useful when you need a function to retain state across multiple calls, without using global variables.

### How Closures Work
Closures are created when:  
1. There is a nested function.
2. The nested function references a value in its enclosing scope.
3. The enclosing function returns the nested function.


## How Closures Work Internally?
When a closure is created, Python internally stores a reference to the environment (variables in the enclosing scope) where the closure was defined. This allows the inner function to access those variables even after the outer function has completed.

In simple terms, a closure “captures” the values from its surrounding scope and retains them for later use. This is what allows closures to remember values from their environment.

## Use of Closures
Encapsulation: Closures help encapsulate functionality. The inner function can access variables from the outer function, but those variables remain hidden from the outside world.
State Retention: Closures can retain state across multiple function calls. This is especially useful in situations like counters, accumulators, or when you want to create a function factory that generates functions with different behaviors.
Functional Programming: Closures are a core feature of functional programming. They allow you to create more flexible and modular code by generating new behavior dynamically.