class Person:
    pass

# objext of class
obj = Person()

# setting attributes for Person class.
setattr(obj,'name','Shubham Biruly')
setattr(obj,'age',25)

# printing
print(obj.name)     # Shubham Biruly
print(obj.age)      # 25

############################################################
# practical example
class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# Example configuration data
config_data = {
    'host': 'localhost',
    'port': 8080,
    'debug': True
}

# Create a Config object and set attributes dynamically
config = Config(**config_data)

# Access the attributes to verify
print(config.host)  # Output: localhost
print(config.port)  # Output: 8080
print(config.debug) # Output: True