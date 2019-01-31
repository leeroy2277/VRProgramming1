import csv

answer = 0
file1 = "biostats.csv"
with open(file1,"r") as file_contents:
    csv_reader = csv.reader(file_contents)

    next(csv_reader)

    percentage = []
    Male = 0
    Female = 0
    counter = 0


    for line in csv_reader:

        percentage.append((line[1]))
        counter += 1

    for line in percentage:
        if line == 'M':
            Male += 1
        else:
            Female += 1

male_percentage = Male/counter
female_percentage = Female/counter


print("the Male percentage is: " + "{:0,.2f}".format(male_percentage * 100) + "%")
print("the Female percentage is: " + "{:0,.2f}".format(female_percentage * 100) + "%")



#print(percentage)
#print(Male)
#print(Female)
#print(counter)
