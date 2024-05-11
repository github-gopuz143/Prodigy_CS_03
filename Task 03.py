import re

def password_complexity_checker(password):

    #length
    length_score = len(password) >= 10

    #uppercase letters
    uppercase_score = bool(re.search(r'[A-Z]', password))

    #lowercase letters
    lowercase_score = bool(re.search(r'[a-z]', password))

    #digits
    digit_score = bool(re.search(r'[0-9]', password))

    #special characters
    special_char_score = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))


    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score


    if total_score == 5:
        return "Strong password"
    elif total_score >= 3:
        return "Good password"
    else:
        return "Weak password"

password = input("Enter your password: ")
strength = password_complexity_checker(password)
print(f"Password strength: {strength}")
