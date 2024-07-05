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

def list_of_rgb_colors():
    rgb = []
    for _ in range(3):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        col = f'rgb({r},{g},{b})'
        rgb.append(col)
    return rgb


if __name__ == '__main__':
    print(list_of_hexa_colors())
    print(list_of_rgb_colors())