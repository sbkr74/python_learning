## GIL (Global Interpreter Lock)
GIL locks the interpreter to execute only single thread at time. So all the code written in `multi-threaded architecture` will effectively converted to `single thread` which slows down or degrade the overall performance of an application.

## Race condition
When we create an object and multiple variable are referencing to that object. Now if the multiple threads holds the reference to a common object which can be either global or modular level object.Therefore, refcount will be based on threads referencing to common object.

for example if there are two threads (T1,T2) pointing at common object (O). so there refcount will be 2.
Now the problem arises when both threads tries to release the reference to that particular object and decrementing the refcount at the same time.  
This raise the problem known as Race Condition.

---

## IO bound
If threads are IO bound then GIL works fine otherwise it would problem. For Soultion we will go next part.