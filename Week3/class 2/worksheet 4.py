import decimal

total = 34.00
increase_rate = 15.56

sd1 = decimal.Decimal(total)
sd2 = decimal.Decimal(increase_rate)

result = (total*increase_rate)
result2 = (result * .001)

print("The total amount increased by the percentage rate is :" + str(result2))

