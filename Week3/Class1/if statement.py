mynumber = 42

if mynumber == 42:
    print("matched")
else:
    print("not a match")

mynumber = 412

if mynumber == 42:
    print("The number " + str(mynumber) + "is greater than 42")
else:
    print("The number" + str(mynumber) + "is less than or equal to 42")

myvalue = 34

if myvalue > 20 and myvalue != 33:
    print("the number is above 20 and its not 33.")