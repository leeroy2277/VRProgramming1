a = input("What age did I start to work?")
b = input("What age are you now?")

try:
    c = int(b) - int(a)
except ValueError:
    print("must enter a number")
else:
    print ("You have been working for {0} years".format(c))

