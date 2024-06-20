import os

# Path to the directory
directory_path = 'Data'

try:
    # List contents of the directory
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        
        if os.path.isfile(entry_path):
            # Perform operations on the file
            with open(entry_path, 'rb') as file:
                print(f"Reading {entry_path}:")
                print(file.read())
        else:
            print(f"{entry_path} is not a file.")
except PermissionError as e:
    print(f"Permission error: {e}")
except FileNotFoundError as e:
    print(f"File not found error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
