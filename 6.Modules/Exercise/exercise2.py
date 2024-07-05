import random
import string
def list_of_hexa_colors():
    s = string.ascii_lowercase
    n = string.digits
    hexa = []
    for _ in range(3):
        hexacode = '#'+''.join(random.choice(s[0:6]+n) for _ in range(6))
        hexa.append(hexacode)
    return hexa


if __name__ == '__main__':
    print(list_of_hexa_colors())