import random

my_list =[]





for x in range(20):
    rand_val = random.randint(1, 20)
    if rand_val == random.randint(1, 20) :
        rand_valCompare = random.randint(1, 20)
        while rand_val == rand_valCompare:
            #print("same")
            rand_val = random.randint(1, 20)
            #print(rand_val)
            continue

    my_list.append(rand_val)


my_list.sort()

print(my_list)





'''

max_of = my_list[0]
min_of = my_list[0]
sum_of = 0
length_of = 0

for x in my_list:
    length_of += 1
    sum_of += x

    if x > max_of:
        max_of = x

    if x < min_of:
        min_of = x

print("Sum =" + str(sum_of))
print("Size =" + str(length_of))
print("Largest =" + str(max_of))
print("Smallest =" + str(min_of))

average_of = sum_of/length_of

print("Average =" + str(average_of))


'''