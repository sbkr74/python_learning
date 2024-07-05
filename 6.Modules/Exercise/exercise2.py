import random
import string
def list_of_hexa_colors(num=3):
    s = string.ascii_lowercase
    n = string.digits
    hexa = []
    for _ in range(num):
        hexacode = '#'+''.join(random.choice(s[0:6]+n) for _ in range(6))
        hexa.append(hexacode)
    return hexa

def list_of_rgb_colors(n=3):
    rgb = []
    for _ in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        col = f'rgb({r},{g},{b})'
        rgb.append(col)
    return rgb

def generate_colors(code,num):
    if code == 'hexa':
        return list_of_hexa_colors(num)
    else:
        return list_of_rgb_colors(num)

if __name__ == '__main__':
    print(list_of_hexa_colors())
    print(list_of_rgb_colors())
    print(generate_colors('hexa',5))