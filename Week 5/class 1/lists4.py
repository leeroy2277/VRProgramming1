my_list = [11, 22, 33, 44]

for item in my_list:
    print(item)

#-----------------------------
for a in range (2, 11, 2):
    print(a)

#-------------------------------

squares = [value**2 for value in range(1,11)]
print(squares)

#-----------------------------------------------

#
my_list_2 = [value * 11 for value in range(1,5)]
print(my_list_2)

#-------------first 10 value of 2**n--------------

my_list_3 = [2 ** n for n in range(11)]
print(my_list_3)

#-----------------------------------------------

car_inspections = [[True, False, True],[True, True, True], [False, False, False], [True, True, True]]

count = 0

for car in car_inspections:
    count += 1
    print("inspection for car number " + str(count))
    print("Inspector 1 : " + str(car[0]))
    print("Inspector 2 : " + str(car[1]))
    print("Inspector 3 : " + str(car[2]))
    print()

#--------------------------------------------------

a = [22, 33]
print(a)
b = (22, 33)
print(b)


#-------------------------------------------
