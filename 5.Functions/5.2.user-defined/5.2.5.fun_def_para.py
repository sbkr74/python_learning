def greetings (name = 'NAME'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Shubham'))

def generate_full_name (first_name = 'first_name', last_name = 'last_name'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Shubham','Biruly'))

def calculate_age (birth_year,current_year = 2024):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1999))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

