import csv

new_contents = []


with open("biostats2.csv", "r") as input_file:
    csv_lines = csv.reader(input_file)

    for line in csv_lines:
        new_contents.append(line)

counter = 1
for r in new_contents:
    if counter == 1:
        r[3] = ''
        r[4] = float(r[4]) * 0.45
        pass
    else:
        r[3] = float(r[3]) * 2.54
        r[4] = float(r[4]) * 0.45
    counter += 1


with open("biostats_write.csv", "w+") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(new_contents)