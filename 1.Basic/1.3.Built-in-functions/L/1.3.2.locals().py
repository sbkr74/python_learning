def example_function():
    a = 10
    b = 20
    print(locals())

example_function()

######################################################################
# CONFIGURATION OF DB CONNECTION
def configure_session(user_input):
    # Default configurations
    db_host = 'localhost'
    db_port = 5432
    debug_mode = False
    theme = 'light'

    # Update configurations based on user input
    for key, value in user_input.items():
        if key in locals():
            locals()[key] = value

    # For demonstration purposes, print the updated configurations
    config = {key: value for key, value in locals().items() if key != 'user_input'}
    return config

# User input that needs to update the configuration
user_input = {
    'db_host': '192.168.1.100',
    'debug_mode': True,
    'theme': 'dark'
}

updated_config = configure_session(user_input)
print(updated_config)
# Output: {'db_host': '192.168.1.100', 'db_port': 5432, 'debug_mode': True, 'theme': 'dark'}

#######################################################################################
# Updating user-profile
def update_user_profile(user_profile, user_input):
    # Update user profile based on input
    for key, value in user_input.items():
        if key in locals():
            locals()[key] = value

    # For demonstration purposes, print the updated profile
    updated_profile = {key: value for key, value in locals().items() if key not in ['user_profile', 'user_input']}
    return updated_profile

# Example user profile
user_profile = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'age': 30,
    'address': '1234 Elm Street'
}

# Example user input from form
user_input = {
    'email': 'john.newemail@example.com',
    'age': 31,
    'address': '5678 Oak Street'
}

updated_profile = update_user_profile(user_profile, user_input)
print(updated_profile)

