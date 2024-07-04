import random as r
import string as s
def random_user_id():
    alpha = s.ascii_lowercase + s.digits
    user_id = ''.join(r.choice(alpha) for _ in range(6))
    return user_id

def user_id_gen_by_user():
    len_of_id,no_of_id = map(str,input().split())
    alpha = s.ascii_lowercase + s.digits
    user_id = []
    for _ in range(int(no_of_id)):
        ids = ''.join(r.choice(alpha) for _ in range(int(len_of_id)))
        user_id.append(ids)    
    for id in user_id:
        print(id)

def rgb_color_gen():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    return f"rgb({red},{green},{blue})"

if __name__ == "__main__":
    print(random_user_id())
    user_id_gen_by_user()
    print(rgb_color_gen())