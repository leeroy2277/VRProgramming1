import csv

#with open ("Sales_Records.csv", 'r') as contents:
 #   contents_lines = contents.read()
  #  print(contents_lines)



#class X:
    #def __init__(self, a):
        #self.a = a

row_counter = 1
unique_types = set()
europe_orders = 0
total_units_sold = 0


with open('Sales_Records.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row_counter != 1:
            unique_types.add(row[2])
            total_units_sold += int(row[8])
            if row[0] == "Europe":


                europe_orders += 1

        row_counter += 1

print("Total units sold {0}" + format(total_units_sold))
print("europe {0}".format(europe_orders))
print('')

print("unique:")

list_counter = 1
for x in unique_types:
    print(str(list_counter) + " " + x)
    list_counter += 1




