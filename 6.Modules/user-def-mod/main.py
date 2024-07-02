import mymodule as m
from mymodule import location as loc
greet =m.greet(m.full_name,"Shubham","Biruly")
print(greet)
department = m.depart('IT')
print(m.full_name("Shubham","Biruly")+" works in "+department)
salary = m.salary('Junior Associate',m.depart('IT'))
print("Initial Salary:",salary)
print("Associate Salary:",m.salary("Associate",m.depart("Dev")))
print(loc("Hyderabad"))