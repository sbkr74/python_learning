import mymodule as m
greet =m.greet(m.full_name,"Shubham","Biruly")
print(greet)
department = m.depart('IT')
print(m.full_name("Shubham","Biruly")+" works in "+department)
salary = m.salary('Junior Associate',m.depart('IT'))
print(salary)
print("Associate Salary",m.salary("Associate",m.depart("Dev")))