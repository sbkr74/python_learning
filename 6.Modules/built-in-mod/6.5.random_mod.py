from random import random, randint, randrange, choice
print(random())
print(randint(5,20))
print(randrange(5,20,3))

# Complex Examples
dice_rolls = [randint(1, 6) for _ in range(2)]
print(dice_rolls)

# Password generator
import string

characters = string.ascii_letters + string.digits + string.punctuation
random_password = ''.join(choice(characters) for _ in range(10))
print(random_password)