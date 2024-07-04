import random as r
import string as s
def random_user_id():
    alpha = s.ascii_lowercase + s.digits
    user_id = ''.join(r.choice(alpha) for _ in range(6))
    return user_id

if __name__ == __name__:
    print(random_user_id())