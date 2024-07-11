# function as parameter
def sum_of_num(nums):
    return sum(nums)

def higher_order_function(f,lst):
    total = f(lst)
    return total

result = higher_order_function(sum_of_num,[1,2,3,4,5])
print(result)

