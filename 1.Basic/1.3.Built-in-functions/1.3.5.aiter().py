# import asyncio

# # Define an asynchronous generator function
# async def async_generator():
#     for i in range(5):
#         # Simulate some asynchronous operation
#         await asyncio.sleep(1)
#         yield i

# # Define an asynchronous function to consume the asynchronous iterable
# async def consume_async_iterable():
#     async for item in async_generator():
#         print(item)

# # Define a coroutine to demonstrate the usage of aiter()
# async def main():
#     # Create an asynchronous iterable using aiter() from the asynchronous generator
#     async_iterable = async_generator()
    
#     # Create an asynchronous iterator from the asynchronous iterable
#     async_iterator = aiter(async_iterable)
    
#     # Use async for loop to consume items from the asynchronous iterator
#     async for item in async_iterator:
#         print(item)

# # Run the event loop
# asyncio.run(main())

#================================================================================================================
# Example1:
async def async_gen():
    for i in range(10):
        yield i

async_iter = aiter(async_gen())
print(type(async_iter))

async def async_iter():
    # async for i in async_iter:
    # for i in async_gen():
    # async for i in async_gen():
    #     print(i)
    for i in range(10):
        yield i
async_obj = aiter(async_iter())
