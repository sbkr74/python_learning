# format()	formats string into nicer output    
lang = 'Python'
program = 'Programming'
days = 30
course = 'Python course'
start = 'Basic'
end = 'Advance'
sentence = 'Learn {} {} in {} days. I will guide you through the {} from {} to {}.'.format(lang, program, str(days), course, start, end)
print(sentence) # Learn Python Programming in 30 days. I will guide you through the Python course from Basic to Advance.

radius = 10
pi = 3.14
area = pi*(radius**2)
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0