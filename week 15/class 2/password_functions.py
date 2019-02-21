import re

def validate_password_complexity(password: str):

    complex_enough = validate_password_length(password)

        # if not re.match("[a-z]", password):
        #     #Lower
        #     complex_enough = False
        #
        # if not re.match("[A-Z]", password):
        #     #Upper
        #     complex_enough = False
        #
        # if not re.match("\d", password):
        #     # Number
        #     complex_enough = False
        #
        # if not re.match("[^0-9A-Za-z\s]", password):
        #     # Special character
        #     complex_enough = False
        #
        # if re.match("\s", password):
        #     # Whitespace
        #     complex_enough = False

    return complex_enough

def validate_password_length(password: str):

    if not re.match("^.{8,}", password):
        #At least 8 long
        return False

    return True