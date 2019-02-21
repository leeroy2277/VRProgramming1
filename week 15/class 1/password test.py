import re


def validate_password_complexity(A ,B):


    if re.match(A,B):
        print('secure password')

    else:
        print("Password must contain at least 8 charactors including, lower, Upper, numbers and a symbol")

A = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})(\s)"

B = input("Enter a password:")

Test = validate_password_complexity(A,B)