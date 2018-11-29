def is_number_negative(n):
    if n < 0:
        return True
    return False

the_number = input("enter a number :")

if is_number_negative(int(the_number)):
    print("negative")
else:
    print("positive")