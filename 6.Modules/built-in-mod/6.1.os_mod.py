import os
# Getting current working directory
print(os.getcwd())

# Creating a directory
# os.mkdir('Extras')

# Changing the current directory
os.chdir('Extras')
print(os.getcwd())

os.mkdir('Test')

# Removing directory
os.rmdir('Test')

# Changing the current directory
os.chdir('../')
print(os.getcwd())
os.rmdir("Extras")
