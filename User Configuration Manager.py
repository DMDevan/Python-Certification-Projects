import re

test_settings = {
        "color": "Blue",
        "volume": 6,
        "security": "Low",
        "notifications": "ON",
        "level": 1
    }

def add_setting(test_settings, pair): 
    key, value = pair
    key = key.lower()
    value = value.lower()
    
    if key in test_settings:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")

    test_settings[key] = value
    return(f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(test_settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key not in test_settings:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
    
    test_settings[key] = value
    return(f"Setting '{key}' updated to '{value}' successfully!")
    
def delete_setting(test_settings, key):
    key = key.lower()

    if key in test_settings:
        del(test_settings[key])
        return(f"Setting '{key}' deleted successfully!")

    return("Setting not found!")

def view_settings(test_settings):
    if not test_settings:
        return("No settings available.")
    
    settings = ""
    for key, value in test_settings.items():
        settings += f"{key.capitalize()}: {value}\n"
    
    return(f"Current User Settings:\n{settings}")