import csv

answer = 0
file1 = "biostats.csv"
with open(file1,"r") as file_contents:
    csv_reader = csv.reader(file_contents)

    next(csv_reader)

    line_counter = 0

    for line in csv_reader:
        answer += (int(line[2]))
        line_counter += 1

    average = answer/line_counter

    print(average)