# Raised when an operation or function receives an argument that has the right type but an inappropriate value.
# def get_positive_integer():
#     while True:
#         try:
#             number = int(input("Please enter a positive integer: "))
#             if number <= 0:
#                 raise ValueError("The number must be a positive integer.")
#             return number
#         except ValueError as e:
#             print("Invalid input:", e)

# if __name__ == "__main__":
#     positive_integer = get_positive_integer()
#     print("You entered a positive integer:", positive_integer)
# ==========================================================

# to view value error just press enter or any value which is not integer
while True:
    num = int(input("Enter a number: "))
    try:
        if num>10:
            print(num)
    except ValueError as e:
        print("Invalid input:", e)