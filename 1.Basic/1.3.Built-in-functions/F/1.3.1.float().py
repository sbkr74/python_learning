# Return a floating point number constructed from a number or string x.
# used for converting string or integer to floating point value. 
x = -10
print(float(x))
s = '12'
print(float(s))

s1 = '+12.787'
print(float(s1))

s2 = 'NaN'
print(float(s2))

#######################################################
def convert_to_float(value):
    try:
        # Strip leading and trailing whitespace
        value = value.strip()
        
        # Convert the string to a float
        number = float(value)
        
        return number
    except ValueError:
        return "Invalid input"

# Examples
print(convert_to_float("  +1000.50  "))  # Output: 1000.5
print(convert_to_float("-500.25"))      # Output: -500.25
print(convert_to_float("NaN"))          # Output: nan (Not a Number)
print(convert_to_float("Infinity"))     # Output: inf (Positive Infinity)
print(convert_to_float("-Infinity"))    # Output: -inf (Negative Infinity)
