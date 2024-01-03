#!/usr/bin/env python3

import re

def validate_user(username, min_length):
    # Check if the username has at least the specified minimum length
    if len(username) < min_length:
        return False

    # Check if the username starts with an alphabetic character or an underscore
    if not re.match(r'^[a-zA-Z_]', username):
        return False

    # Check if the username contains only alphanumeric characters, underscores, or dots
    if not re.match(r'^[a-zA-Z0-9_.]+$', username):
        return False

    return True

# Test cases
print(validate_user("blue. Kale", 3))  # True
print(validate_user(".blue.kale", 3))  # False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4)) # False

