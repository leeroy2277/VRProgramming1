import decimal

sale1 = "1.40"
sale2 = "2.30"

sd1 = decimal.Decimal(sale1)
sd2 = decimal.Decimal(sale2)

result = (sd1 + sd2)

print ("the total price is $" + str(result))