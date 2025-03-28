from datetime import date
try:
    name = input("Enter Your Name: ")
    born_year = input("Enter year you are born: ")
    age = date.today().year - int(born_year)
    print(f"Hello {name}, now your age is {age}.")
except Exception as e:
    print("Error:",e)
finally:
    print("I will always run.")


try:
    name = input("Enter Your Name: ")
    year_of_grad = input("Enter year you wore graduated: ")
    exp = date.today().year - int(year_of_grad)
    print(f"Hello {name}, you have graduated {exp} years ago.")
except Exception as e:
    print("Error:",e)
else:
    print("Getting used to work with try block")
finally:
    print("I will always run.")