import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for uppercase and lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one number."

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Your password is strong!"

# Input from the user
password = input("Enter your password: ")
print(check_password_strength(password))
