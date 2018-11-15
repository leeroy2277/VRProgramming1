x = input("enter a number  >")
y = input("enter another number  >")
z = int(x)/int(y)

try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("sorry you cannot divide by zero")
else:
    print(result)
