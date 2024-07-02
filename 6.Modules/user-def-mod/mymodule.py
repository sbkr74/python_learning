def full_name(firstname,lastname):
    return firstname+' '+lastname

def greet(f,fname,lname):
    msg = "Hi, "+f(fname,lname)+"! Good Morning"
    return msg

def depart(dept):
    return dept + ' department'

def salary(pos,depart):
    if depart == 'IT department' and pos == 'Junior Associate':
        return 600000
    elif depart == 'IT department' and pos == 'Associate':
        return 1000000
    elif depart == 'IT department' and pos == 'Senior Associate':
        return 1800000
    elif depart == 'Dev department' and pos == 'Junior Associate':
        return 800000
    elif depart == 'Dev department' and pos == 'Associate':
        return 2400000
    elif depart == 'Dev department' and pos == 'Senior Associate':
        return 3800000
    else:
        return "not in database."