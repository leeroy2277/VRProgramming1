def calculate_tax(amount):
    amount_with_tax = amount * 1.1556
    return amount_with_tax

value =100
print("The value is " + str(value))
value_with_tax = calculate_tax(value)
print ("The value with tax is " + str(value_with_tax))


