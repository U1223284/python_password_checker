# This is a simple password checker. You can run the file from the terminal. You can simply just
# run the program from an IDE that has a python execution environment.
# @author Tayvon Chamale
# @version 02/20/2025

import re
""" The following method is used to check the strength of a password entered from the user.
It give the password passed a score based on the following criteria:
    1. If the length is greater than 8 characters.
    2. If the password contains uppercase letters.
    3. If the password contains lowercase letters.
    4. If the password contains digits.
    5. If the password contains special characters.
The method will return a string that describes the strength of the password based on the strength score.
"""
def check_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'\d', password) is not None,
        "special_char": re.search(r'[@$!%*?&]', password) is not None
    }

    for passed in criteria.values():
        if passed:
            strength += 1

    if strength <= 2:
        return "Weak Password"
    elif strength == 3 or strength == 4:
        return "Moderate Password"
    else:
        return "Strong Password"


if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")
    result = check_password_strength(user_password)
    print(f"Password Strength: {result}")