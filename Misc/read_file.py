import re

# Reading .py file and storing its content
file_path = 'Data\countries.py'

with open(file_path, 'r') as file:
    content = file.read()

# Using regular expressions to find the list of countries
pattern = r'\[([^\[\]]*)\]'
matches = re.findall(pattern, content)

# Extracting the list of countries from the matches
if matches:
    countries_str = matches[0]
    # Remove unwanted characters
    countries_str = countries_str.replace("\n", "").replace('"', "")
    countries = [country.strip().strip("'") for country in countries_str.split(",") if country.strip()]
    cleaned_countries = []
    for country in countries:
        cleaned_countries.append(country)
    print(cleaned_countries)
else:
    print("No list of countries found in the file.")