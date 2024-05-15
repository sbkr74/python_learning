# replace() is used to replace the substring inside the string 
string = 'python programming from Basic to Advance'
print(string.replace('programming','coding'))

# user input ones
user_input = input("Enter your text: ")
sub , rep = map(str,input().split())
print(user_input.replace(sub,rep))