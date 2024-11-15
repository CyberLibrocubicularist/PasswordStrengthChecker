import string

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    strength_level = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    if strength_level == 5:
        return "Very Strong"
    elif strength_level == 4:
        return "Strong"
    elif strength_level == 3:
        return "Moderate"
    elif strength_level == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

