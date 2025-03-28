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