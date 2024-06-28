def full_name(firstname,lastname):
    return firstname+' '+lastname

def greet(f,fname,lname):
    msg = "Hi, "+f(fname,lname)+"! Good Morning"
    return msg

def depart(dept):
    return dept + ' department'
